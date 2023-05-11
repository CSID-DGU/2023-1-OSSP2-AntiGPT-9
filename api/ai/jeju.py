import json
import pickle

from transformers import (
    PreTrainedTokenizerFast as BaseGPT2Tokenizer,
    EncoderDecoderModel,
    DataCollatorForSeq2Seq,
)
from tokenization_kobert import KoBertTokenizer

class GPT2Tokenizer(BaseGPT2Tokenizer):
    def build_inputs_with_special_tokens(self, token_ids, _):
        return token_ids + [self.eos_token_id]

trg_tokenizer = GPT2Tokenizer.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
src_tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')

with open('./save_src_tk.pickle','rb') as f:
    src_tokenizer = pickle.load(f)

model = EncoderDecoderModel.from_pretrained('leadawon/ossp-v0_3')
model.eval()
model.config.decoder_start_token_id = trg_tokenizer.bos_token_id


def translate(text):
    embeddings = src_tokenizer(text, return_attention_mask=False, return_token_type_ids=False, return_tensors='pt')
    embeddings = {k: v for k, v in embeddings.items()}
    output = model.generate(**embeddings)[0, 1:-1]
    tmp = trg_tokenizer.decode(output.cpu())
    print(tmp)
    return tmp

if __name__=="__main__":
    translate("속앗수다예")
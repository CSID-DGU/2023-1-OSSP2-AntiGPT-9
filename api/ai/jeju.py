import json

from transformers import (
    PreTrainedTokenizerFast as BaseGPT2Tokenizer,
    EncoderDecoderModel,
)
from .tokenization_kobert import KoBertTokenizer


'''class GPT2Tokenizer(BaseGPT2Tokenizer):
    def build_inputs_with_special_tokens(self, token_ids, _):
        return token_ids + [self.eos_token_id]


trg_tokenizer = GPT2Tokenizer.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')


src_tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert', from_tf=True)
with open("./added_tokens.json", 'rb') as f:
    dw_dict = json.load(f)
dict_swap = {v: k for k, v in dw_dict.items()}

for i in range(8002, 12291):
    src_tokenizer.add_tokens(dict_swap[i])

model = EncoderDecoderModel.from_pretrained('leadawon/ossp-v0_3')
model.eval()
model.config.decoder_start_token_id = trg_tokenizer.bos_token_id


def translate(text):
    embeddings = src_tokenizer(text, return_attention_mask=False, return_token_type_ids=False, return_tensors='pt')
    embeddings = {k: v for k, v in embeddings.items()}
    output = model.generate(**embeddings)[0, 1:-1]
    tmp = trg_tokenizer.decode(output.cpu())
    return tmp'''


# Jeju To Standard translate Class
class JejuToStandard:

    class GPT2Tokenizer(BaseGPT2Tokenizer):
        def build_inputs_with_special_tokens(self, token_ids, _):
            return token_ids + [self.eos_token_id]

    trg_tokenizer = GPT2Tokenizer.from_pretrained("skt/kogpt2-base-v2", bos_token='</s>', eos_token='</s>',
                                                  unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')

    src_tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert', from_tf=True)
    with open("ai/added_tokens.json", 'rb') as f:
        dw_dict = json.load(f)
    dict_swap = {v: k for k, v in dw_dict.items()}

    for i in range(8002, 12291):
        src_tokenizer.add_tokens(dict_swap[i])

    model = EncoderDecoderModel.from_pretrained('leadawon/ossp-v0_3')
    model.eval()
    model.config.decoder_start_token_id = trg_tokenizer.bos_token_id


    def translate(self, text):
        embeddings = self.src_tokenizer(text, return_attention_mask=False, return_token_type_ids=False, return_tensors='pt')
        embeddings = {k: v for k, v in embeddings.items()}
        output = self.model.generate(**embeddings)[0, 1:-1]
        tmp = self.trg_tokenizer.decode(output.cpu())
        return tmp.strip()


# Standard to Jeju translate Class
class StandardToJeju:
    class GPT2Tokenizer(BaseGPT2Tokenizer):
        def build_inputs_with_special_tokens(self, token_ids, _):
            return token_ids + [self.eos_token_id]

    trg_tokenizer = GPT2Tokenizer.from_pretrained("skt/kogpt2-base-v2", bos_token='</s>', eos_token='</s>',
                                                  unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')

    src_tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert', from_tf=True)
    # standard to jeju
    with open("ai/added_tokens_trg.json",'rb') as f:
        dw_dict_trg = json.load(f)
    dict_swap_trg = {v: k for k, v in dw_dict_trg.items()}
    ma = 54000
    mi = 51200
    for i in range(51200, 54001):
        trg_tokenizer.add_tokens(dict_swap_trg[i])

    stj_model = EncoderDecoderModel.from_pretrained('leadawon/ossp-reverse-v0_3')
    stj_model.eval()
    stj_model.config.decoder_start_token_id = trg_tokenizer.bos_token_id

    def translate(self, text):
        embeddings = self.src_tokenizer(text, return_attention_mask=False, return_token_type_ids=False, return_tensors='pt')
        embeddings = {k: v for k, v in embeddings.items()}
        output = self.stj_model.generate(**embeddings)[0, 1:-1]
        tmp = self.trg_tokenizer.decode(output.cpu())
        return tmp.strip()

'''if __name__ == "__main__":
    jeju = Jeju # test code
    print(f"'{jeju.translate(jeju,'속았수다')}'")'''
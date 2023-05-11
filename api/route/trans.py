from fastapi import APIRouter, HTTPException, status
from ..model.sentence import sentence

trans_router = APIRouter(
    tags=['trans']
)


#translator router
@trans_router.post("/trans",response_model=sentence)
async def translator(body: sentence) -> dict:
    if sentence is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="empty"
        )
    #jeju to standard
    #trans = #번역모델
    #데이터 베이스 저장
    return { "standard": f"{'''trans'''}"}

#query search router
#query list get router
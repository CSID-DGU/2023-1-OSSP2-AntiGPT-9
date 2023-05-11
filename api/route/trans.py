from fastapi import APIRouter, HTTPException, status
from ..model.sentence import sentence

trans_router = APIRouter(
    tags=['jeju']
)


#translator router
@trans_router.post("/trans",response_model=sentence)
async def translator(body: sentence) -> dict:
    if sentence is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="empty"
        )
    #번역
    trans = #번역모델
    #데이터 베이스 저장

    return { "standard": f"{trans}"}
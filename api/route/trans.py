from fastapi import APIRouter, HTTPException, status
from ai.jeju import Jeju
from model.sentence import Dialect
from typing import Optional
# 모델 실행
model = Jeju

trans_router = APIRouter(
    tags=['trans']
)


# translator router
@trans_router.post("/jeju")
async def translator(dialect: Dialect) -> dict:
    if dialect is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="empty"
        )
    # 번역
    standard = model.translate(model, dialect.dialect)
    print(f"'{standard}'")

    # 반환(json)
    return {"standard": f"{standard}"}


# query search router

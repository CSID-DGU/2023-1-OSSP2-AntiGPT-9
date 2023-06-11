from fastapi import APIRouter, HTTPException, status
from ai.jeju import JejuToStandard, StandardToJeju
from model.sentence import Dialect, Standard
from typing import Optional
# 모델 실행
model = JejuToStandard
stj_model = StandardToJeju
trans_router = APIRouter(
    tags=['trans']
)


# translator router
@trans_router.post("/tostandard")
def translator(dialect: Dialect) -> dict:
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

@trans_router.post("/tojeju")
def translator(standard: Standard) -> dict:
    if standard is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="empty"
        )
    # standard to jeju
    jeju = stj_model.translate(stj_model, standard.standard)

    return {"jeju":f"{jeju}"}
# query search router

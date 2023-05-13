from fastapi import APIRouter, HTTPException, status
from ai.jeju import Jeju
from pydantic import BaseModel
from typing import Optional
# 모델 실행
model = Jeju

trans_router = APIRouter(
    tags=['trans']
)


class Dialect(BaseModel):
    dialect: str
    test: Optional[str]


# translator router
@trans_router.post("/jeju")
async def translator(dialect: Dialect) -> dict:
    if dialect is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="empty"
        )
    standard = model.translate(model, dialect.dialect)
    print(f"'{standard}'")
    # 데이터 베이스 저장 (later)
    return {"standard": f"{standard}"}

# query search router

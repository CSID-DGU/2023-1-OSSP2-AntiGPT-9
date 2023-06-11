from pydantic import BaseModel


class Dialect(BaseModel):
    # 방언 데이터 수신
    dialect: str


class Standard(BaseModel):
    # 번역할 데이터 수신
    standard: str

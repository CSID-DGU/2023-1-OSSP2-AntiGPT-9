from pydantic import BaseModel


class Dialect(BaseModel):
    dialect: str


class Standard(BaseModel):
    standard: str
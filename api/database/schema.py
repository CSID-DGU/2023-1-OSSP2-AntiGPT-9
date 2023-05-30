import datetime
from pydantic import BaseModel


class sentence(BaseModel):
    id: int
    jeju: str
    standard: str
    created_at: datetime.datetime

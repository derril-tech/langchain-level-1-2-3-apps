from pydantic import BaseModel
from typing import Optional

class PDFRequest(BaseModel):
    name: str
    selected: bool
    file: str

class PDFResponse(BaseModel):
    id: int
    name: str
    selected: bool
    file: str

    class Config:
        orm_mode = True  # ✅ Enables from_orm() for SQLAlchemy models

# ✅ For PDF Question Answering
class QuestionRequest(BaseModel):
    question: str

from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionCreate(BaseModel):
    amount: float
    type: str  # INCOME / EXPENSE
    category: str
    date: date
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    description: Optional[str]

    class Config:
        from_attributes = True
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas.transaction_schema import TransactionCreate, TransactionResponse
from services.transaction_service import create_transaction, get_transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse)
def create_transaction_route(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return create_transaction(db, transaction)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions_route(
    type: str = Query(None),
    category: str = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_transactions(db, type, category, skip, limit)
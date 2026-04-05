from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from fastapi import HTTPException
from database import get_db
from schemas.transaction_schema import TransactionCreate, TransactionResponse
from services.transaction_service import create_transaction, get_transactions
from utils.auth import get_role, require_admin
from services.transaction_service import update_transaction, delete_transaction
from datetime import date
router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse)
def create_transaction_route(
    transaction: TransactionCreate,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    require_admin(role)
    return create_transaction(db, transaction)

@router.get("/", response_model=list[TransactionResponse])
def get_transactions_route(
    type: str = Query(None),
    category: str = Query(None),
    date : date = Query(None),
    skip: int = 0,
    limit: int = 10,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    return get_transactions(db, type, category, date, skip, limit)

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_transaction_route(
    transaction_id: int,
    transaction: TransactionCreate,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    require_admin(role)

    updated = update_transaction(db, transaction_id, transaction)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return updated

@router.delete("/{transaction_id}")
def delete_transaction_route(
    transaction_id: int,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    require_admin(role)

    deleted = delete_transaction(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction deleted"}
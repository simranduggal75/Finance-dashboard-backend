from sqlalchemy.orm import Session
from models.transaction import Transaction
from datetime import date 
from sqlalchemy import func

def create_transaction(db: Session, data):
    transaction = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        description=data.description
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    
    return transaction


def get_transactions(db: Session, type=None, category=None, date=None, skip=0, limit=10):
    query = db.query(Transaction)

    if type:
        query = query.filter(func.lower(Transaction.type) == type.lower())

    if category:
        query = query.filter(func.lower(Transaction.category) == category.lower())

    if date:
        query = query.filter(Transaction.date == date)

    return query.offset(skip).limit(limit).all()

def update_transaction(db: Session, transaction_id: int, data):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None

    transaction.amount = data.amount
    transaction.type = data.type
    transaction.category = data.category
    transaction.date = data.date
    transaction.description = data.description

    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return transaction


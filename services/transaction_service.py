from sqlalchemy.orm import Session
from models.transaction import Transaction


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


def get_transactions(db: Session, type=None, category=None, skip=0, limit=10):
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.offset(skip).limit(limit).all()
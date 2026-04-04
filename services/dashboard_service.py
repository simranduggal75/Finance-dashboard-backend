from sqlalchemy.orm import Session
from models.transaction import Transaction
from sqlalchemy import func

def get_summary(db: Session):
    total_income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == "INCOME"
    ).scalar() or 0

    total_expense = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == "EXPENSE"
    ).scalar() or 0

    balance = total_income - total_expense

    return {
        "totalIncome": total_income,
        "totalExpense": total_expense,
        "balance": balance
    }
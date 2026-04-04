from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.dashboard_service import get_summary

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return get_summary(db)
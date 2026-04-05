from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.dashboard_service import get_summary
from utils.auth import get_role, require_analyst_or_admin

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    require_analyst_or_admin(role)
    return get_summary(db)
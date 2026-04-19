from fastapi import APIRouter, Depends , FastAPI
from sqlalchemy.orm import Session

from database import get_db , engine, Base
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import create_user, get_users
from utils.auth import get_role, require_admin
from models import user, transaction
from routes import user_routes, transaction_routes, dashboard_routes

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user_route(
    user: UserCreate,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    require_admin(role)
    return create_user(db, user.name, user.email, user.role)


@router.get("/", response_model=list[UserResponse])
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)
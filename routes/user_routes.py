from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email, user.role)


@router.get("/", response_model=list[UserResponse])
def get_users_route(db: Session = Depends(get_db)):
    return get_users(db)
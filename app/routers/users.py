from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import crud_user
from app.models import user as user_model
from app.schemas import user as user_schema
from app.base.base_exception import BaseException

router = APIRouter()


@router.post("/", response_model=user_schema.User)
def create_user(
    *, db: Session = Depends(deps.get_db), user_in: user_schema.UserCreate
) -> Any:
    """
    Create new user.
    """
    user = crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise BaseException(
            status_code=400,
            message="The user with this username already exists in the system.",
        )
    user = crud_user.create_user(db, user=user_in)
    return user


@router.get("/me", response_model=user_schema.User)
def read_user_me(
    current_user: user_model.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    return current_user

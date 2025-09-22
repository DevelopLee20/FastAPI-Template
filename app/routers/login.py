from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core import security
from app.crud import crud_user
from app.schemas import token as token_schema
from app.base.base_exception import BaseException

router = APIRouter()


@router.post("/login/access-token", response_model=token_schema.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not security.Security.verify_password(
        form_data.password, user.hashed_password
    ):
        raise BaseException(status_code=400, message="Incorrect email or password")
    elif not user.is_active:
        raise BaseException(status_code=400, message="Inactive user")
    access_token = security.Security.create_access_token(subject=user.email)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

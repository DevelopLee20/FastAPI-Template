from typing import Generator

from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.env import settings
from app.crud import crud_user
from app.db.session import SessionLocal
from app.models import user as user_model
from app.schemas import token as token_schema
from app.base.base_exception import BaseException

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> user_model.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = token_schema.TokenData(**payload)
    except (jwt.JWTError, ValidationError):
        raise BaseException(
            status_code=status.HTTP_403_FORBIDDEN,
            message="Could not validate credentials",
        )
    user = crud_user.get_user_by_email(db, email=token_data.email)
    if not user:
        raise BaseException(status_code=404, message="User not found")
    return user

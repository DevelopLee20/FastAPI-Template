from sqlalchemy.orm import Session

from app.db import base_class, session


def init_db(db: Session) -> None:
    # Tables should be created with Alembic, but for development this is fine
    base_class.Base.metadata.create_all(bind=session.engine)

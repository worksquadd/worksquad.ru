from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    """
    Йилдит новую бд сессию.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

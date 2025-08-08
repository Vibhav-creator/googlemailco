from __future__ import annotations

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
import os

# database URL can be overridden with the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# enable pool_pre_ping for a more stable connection pool
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Base declarative class for all models."""
    pass


def get_db() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

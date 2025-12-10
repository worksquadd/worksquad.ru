from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base


class User(Base):
    # Base automatically generates __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    # Telegram specific fields
    tg_username = Column(String, unique=True, index=True, nullable=True)

    # Internal app fields
    username = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)

    # Profile & Permissions
    picture = Column(String, nullable=True)
    role = Column(String, default="user", nullable=False)

    # Metadata
    # func.now() ensures the DB sets the time, not the Python app
    registry_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

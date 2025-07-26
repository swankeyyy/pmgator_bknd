from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

import uuid


# Init Base model
class Base(DeclarativeBase):
    """Abstract base model for SQLAlchemy with UUID primary key.

    Features:
    - Uses PostgreSQL UUID type by default
    - Generates UUID v4 automatically for new records
    - Provides consistent ID type across all models"""

    __abstract__ = True
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        nullable=False,
    )

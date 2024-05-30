from datetime import UTC, datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import TIMESTAMP, Integer, String, Text


class Base(DeclarativeBase):
    pass


class CreditAgencySummaries(Base):
    __tablename__ = "credit_agency_summaries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rating: Mapped[str] = mapped_column(String(length=10), nullable=False)
    # rating_details: Mapped[str] = mapped_column(String(length=10), nullable=False)
    summary: Mapped[str] = mapped_column(String(length=1000), nullable=False)
    created_at: Mapped[datetime.timestamp] = mapped_column(
        TIMESTAMP, default=datetime.now(UTC)
    )


class TextPressReleases(Base):
    __tablename__ = "text_press_releases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.timestamp] = mapped_column(
        TIMESTAMP, default=datetime.now(UTC)
    )


class ModifiedPressReleases(Base):
    __tablename__ = "modified_press_releases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.timestamp] = mapped_column(
        TIMESTAMP, default=datetime.now(UTC)
    )

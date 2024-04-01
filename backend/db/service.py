from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .connection import async_session
from .models import CreditAgencySummaries, ModifiedPressReleases, TextPressReleases


@asynccontextmanager
async def async_database_session():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()


class UserTextPressRelease:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_release(self, text_release: str) -> bool:
        new_text_release = TextPressReleases(text=text_release)
        self.session.add(new_text_release)

        return True

    async def get_text_press_release(self, id: int):
        filters = [TextPressReleases.id == id]
        query = select(TextPressReleases).where(*filters)

        results = await self.session.execute(query)

        return results.scalars().all()


class CreditAgencySummary:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_summary(self, id: int, rating: str, detail_rating: str, summary: str) -> bool:
        new_summary = CreditAgencySummaries(
            id=id, rating=rating, rating_details=detail_rating, summary=summary
        )
        self.session.add(new_summary)

        return True

    async def get_summaries(self):
        query = select(CreditAgencySummaries)
        credit_agency_symmaries = await self.session.execute(query)

        return credit_agency_symmaries.scalars().all()

class ModifiedPressRelease:
    def __init__(self, session: AsyncSession) -> bool:
        self.session = session

    async def add_modified_press_release(self, modified_text: str):
        new_mod_press_release = ModifiedPressReleases(id=id, text=modified_text)
        self.session.add(new_mod_press_release)

        return True

from db.service import (
    CreditAgencySummary,
    ModifiedPressRelease,
    UserTextPressRelease,
    async_database_session,
)
from schemas import (
    CreditAgencySummariesGet,
    ModifiedPressReleaseGet,
)


async def get_credit_agency_summaries():
    async with async_database_session() as session:
        cas_manager = CreditAgencySummary(session)
        all_credit_agencies = await cas_manager.get_summaries()
        return [
            CreditAgencySummariesGet.model_validate(credit_agencies)
            for credit_agencies in all_credit_agencies
        ]


async def add_credit_agency_summaries(rating: str, summary: str):
    async with async_database_session() as session:
        cas_manager = CreditAgencySummary(session)
        is_added = await cas_manager.add_summary(rating, summary)

        return is_added


async def add_realease(text: str):
    async with async_database_session() as session:
        user_text_rel_manager = UserTextPressRelease(session)
        is_added = await user_text_rel_manager.register_release(text_release=text)

        return is_added


async def add_modified_text_press_release(text: str):
    async with async_database_session() as session:
        mod_test_press_release_manager = ModifiedPressRelease(session)
        is_added = await mod_test_press_release_manager.add_modified_press_release(text)

        return is_added


async def get_modified_text_press_release(id: int):
    async with async_database_session() as session:
        mod_test_press_release_manager = ModifiedPressRelease(session)
        modified_text_press_release = await mod_test_press_release_manager.get_press_release(id)
        if modified_text_press_release is not None:
            return ModifiedPressReleaseGet.model_validate(modified_text_press_release)

        return None


async def get_rating_summary(id: int):
    async with async_database_session() as session:
        cas_manager = CreditAgencySummary(session)
        rating_summary = await cas_manager.get_summary(id)
        if rating_summary is not None:
            return CreditAgencySummariesGet.model_validate(rating_summary)

        return None

from fastapi import APIRouter, HTTPException, status

from celery_task.tasks import preprocessing
from schemas import CreditAgencySummaries, CreditAgencySummariesGet, PressRelease
from service import (
    add_credit_agency_summaries,
    add_realease,
    get_credit_agency_summaries,
    get_modified_text_press_release,
    get_rating_summary,
)

router = APIRouter(prefix="", tags=None)


@router.post("/predict_model")
def predict_model(text_release: PressRelease):
    release = text_release.model_dump()

    # Дописать вызов модели или кладем в очередь на исполнение
    preprocessing.delay(release["text"])

    # if True:
    #     return "Record added successfully"
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add new text release"
    #     )


@router.get("/cra-summaries")
async def get_cra_summaries() -> list[CreditAgencySummariesGet] | None:
    cra_summaries = await get_credit_agency_summaries()
    if len(cra_summaries) == 0:
        return None

    return cra_summaries


@router.post("/cra-summaries")
async def insert_cra_summaries(credit_agency_info: CreditAgencySummaries) -> str:
    credit_agency_data = credit_agency_info.model_dump()
    is_added = await add_credit_agency_summaries(**credit_agency_data)

    if is_added:
        return "Record added successfully"
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to add record")


@router.get("/text_release/{id_release}")
async def get_mod_text_release(id_release: int):
    text_realese = await get_modified_text_press_release(id_release)
    summary_realese = await get_rating_summary(id_release)

    return text_realese, summary_realese

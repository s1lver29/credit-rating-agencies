import asyncio

from celery import Celery

from service import add_credit_agency_summaries, add_modified_text_press_release, add_realease

from .ml.main import generate_report_press_release

celery_app = Celery(
    __name__,
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["celery_task.tasks"],
)

loop = asyncio.get_event_loop()

@celery_app.task
def preprocessing(text: str):
    text_color, report_tfidf, category_rating = generate_report_press_release(text)

    print(text_color)

    try:
        task1 = loop.create_task(add_realease(text))
        task2 = loop.create_task(add_modified_text_press_release(text_color))
        task3 = loop.create_task(
            add_credit_agency_summaries(category_rating, text[:150] + "...")
        )

        group_tasks = asyncio.gather(task1, task2, task3)

        loop.run_until_complete(group_tasks)
    finally:
        loop.close()

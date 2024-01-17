import asyncio

from celery.app import Celery

from application.use_case.celery import CeleryUseCase
from infrastructure.config import get_settings

settings = get_settings()


redis_url = f"redis://{settings.redis_host}:{settings.redis_port}"

celery_app = Celery("binance_parser", broker=redis_url, backend=redis_url)
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "send_tickers_info": {
        "task": "tasks.main.send_tickers_info",
        "schedule": settings.celery_beat_time,
    }
}


@celery_app.task
def send_tickers_info():
    service = CeleryUseCase()

    asyncio.run(service.get_data_and_send())

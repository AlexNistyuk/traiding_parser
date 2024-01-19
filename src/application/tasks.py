import asyncio

import aiohttp
from celery.app import Celery

from infrastructure.config import get_settings

settings = get_settings()


celery_app = Celery(
    "binance_parser", broker=settings.redis_url, backend=settings.redis_url
)
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "send_tickers_info": {
        "task": "application.tasks.send_tickers_info",
        "schedule": settings.celery_beat_time,
        "options": {"queue": settings.celery_queue},
    }
}


@celery_app.task
def send_tickers_info():
    asyncio.run(send_async_request())


async def send_async_request():
    async with aiohttp.ClientSession() as session:
        response = await session.get(settings.coins_update_url)

        return await response.text()

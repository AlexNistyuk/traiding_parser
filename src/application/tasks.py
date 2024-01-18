import asyncio

import aiohttp
from celery.app import Celery

from infrastructure.config import get_settings

settings = get_settings()


redis_url = f"redis://{settings.redis_host}:{settings.redis_port}"

celery_app = Celery("binance_parser", broker=redis_url, backend=redis_url)
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "send_tickers_info": {
        "task": "application.tasks.send_tickers_info",
        "schedule": settings.celery_beat_time,
        "options": {"queue": settings.celery_queue}
    }
}

WEB_URL = f"{settings.web_scheme}://{settings.web_host}:{settings.web_port}"
COINS_ENDPOINT = f"{WEB_URL}{settings.coins_update_endpoint}"


@celery_app.task
def send_tickers_info():
    asyncio.run(send_async_request())


async def send_async_request():
    async with aiohttp.ClientSession() as session:
        response = await session.get(COINS_ENDPOINT)

        return await response.text()

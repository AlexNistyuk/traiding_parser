import asyncio
from parser.services import BinanceAPIService

from celery.app import Celery

from config import get_settings

settings = get_settings()


redis_url = f"redis://{settings.redis_host}:{settings.redis_port}"

celery_app = Celery("binance_parser", broker=redis_url, backend=redis_url)
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "get_tickers_info": {
        "task": "tasks.celery.send_tickers_info",
        "schedule": settings.celery_beat_time,
    }
}


@celery_app.task
def send_tickers_info():
    asyncio.run(get_ticker_info_and_send())


async def get_ticker_info_and_send():
    await BinanceAPIService().connect()
    tickers_info = await BinanceAPIService().get_tickers_info()
    await BinanceAPIService().close()

    print(len(tickers_info[0]))

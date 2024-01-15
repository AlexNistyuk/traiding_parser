import asyncio

from assets.use_case.assets_insert import AssetInsertUseCase
from binances.domain.use_case import IBinanceUseCase
from binances.use_case.binance_use_case import BinanceUseCase
from tasks.domain.celery import ICeleryUseCase


class CeleryUseCase(ICeleryUseCase):
    binance_use_case: IBinanceUseCase = BinanceUseCase()
    asset_insert_use_case = AssetInsertUseCase()

    async def get_data_and_send(self) -> None:
        """Get data from binance API and send it to Kafka and DB"""
        documents = await self.binance_use_case.get_tickers_info()

        db_task = asyncio.create_task(self.asset_insert_use_case.insert_many(documents))

        await db_task

import asyncio

from application.use_case.assets import AssetUseCase
from application.use_case.binances import BinanceUseCase


class CeleryUseCase:
    binance_use_case = BinanceUseCase()
    asset_use_case = AssetUseCase()

    async def get_data_and_send(self) -> None:
        """Get data from binance API and send it to Kafka and DB"""
        documents = await self.binance_use_case.get_tickers_info()

        db_task = asyncio.create_task(self.asset_use_case.insert_many(documents))

        await db_task

import asyncio

from application.use_case.assets import AssetUseCase
from application.use_case.binances import BinanceUseCase
from application.use_case.kafka import KafkaBinanceUseCase
from domain.entities.kafka import KafkaDTO


class CoinUseCase:
    binance_use_case = BinanceUseCase()
    asset_use_case = AssetUseCase()
    kafka_use_case = KafkaBinanceUseCase()

    async def get_data_and_send(self) -> None:
        """Get data from binance API and send it to Kafka and DB"""
        documents = await self.binance_use_case.get_tickers_info()
        kafka_documents = [KafkaDTO(**document).model_dump() for document in documents]

        db_task = asyncio.create_task(self.asset_use_case.insert_many(documents))
        kafka_task = asyncio.create_task(self.kafka_use_case.send(kafka_documents))

        await db_task
        await kafka_task

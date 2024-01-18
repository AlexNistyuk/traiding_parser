import logging

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

logger = logging.Logger(__name__)


settings = get_settings()


class KafkaManager(IManager):
    client: AIOKafkaProducer
    url = f"{settings.kafka_host}:{settings.kafka_port}"

    @classmethod
    async def connect(cls):
        try:
            logger.info("Connect to Kafka")

            cls.client = AIOKafkaProducer(bootstrap_servers=cls.url)
            await cls.client.start()

            return cls
        except KafkaError as exc:
            logger.error(f"Error while connecting to kafka: {exc}")

    @classmethod
    async def close(cls) -> None:
        await cls.client.stop()

        logger.info("Close kafka connection")

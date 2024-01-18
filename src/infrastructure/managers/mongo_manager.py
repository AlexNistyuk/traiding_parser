import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

settings = get_settings()

logger = logging.Logger(__name__)


class Manager(IManager):
    """Database manager which connects to mongodb"""

    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongodb_url)
    db: AsyncIOMotorDatabase = client[settings.mongodb_database]

    @classmethod
    async def connect(cls):
        return cls

    @classmethod
    async def close(cls) -> None:
        cls.client.close()

        logger.info("Close database connection")

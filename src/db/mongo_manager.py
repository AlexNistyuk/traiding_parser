from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config import get_settings

settings = get_settings()


class Manager:
    """Database manager which connects to mongodb"""

    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongodb_url)
    db: AsyncIOMotorDatabase = client[settings.mongodb_database]

    @classmethod
    async def connect(cls):
        return cls

    @classmethod
    async def close(cls):
        cls.client.close()

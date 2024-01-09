from typing import Iterable

from src.db.mongo import db_collection
from src.interfaces import IRepository


class MongoDBRepository(IRepository):
    async def insert_one(self, document: dict):
        return await db_collection.insert_one(document)

    async def insert_many(self, documents: Iterable[dict]):
        return await db_collection.insert_many(documents)

    async def filter(self, filters: dict):
        result = db_collection.find(filters)

        return [document async for document in result]

    async def get_one(self, filters: dict):
        return await db_collection.find_one(filters)

    async def get_all(self):
        return await self.filter({})

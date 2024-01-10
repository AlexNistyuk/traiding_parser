from typing import Iterable

from bson import ObjectId

from db.mongo_manager import Manager
from interfaces.database import IRepository


class BaseRepository(Manager, IRepository):
    """Mongodb base repository with database operations"""

    collection: str

    async def insert_one(self, document: dict):
        return await self.db[self.collection].insert_one(document)

    async def insert_many(self, documents: Iterable[dict]):
        return await self.db[self.collection].insert_many(documents)

    async def get_by_id(self, document_id: str):
        return await self.db[self.collection].find_one({"_id": ObjectId(document_id)})

    async def get_one(self, filters: dict):
        return await self.db[self.collection].find_one(filters)

    async def filter(self, filters: dict):
        return self.db[self.collection].find(filters).to_list(length=None)

    async def get_all(self):
        return self.db[self.collection].find({}).to_list(length=None)

    async def delete_by_id(self, document_id: str):
        return await self.db[self.collection].delete_one({"_id": ObjectId(document_id)})

    async def delete_one(self, filters: dict):
        return await self.db[self.collection].delete_one(filters)

    async def delete_many(self, filters: dict):
        return await self.db[self.collection].delete_many(filters)

    async def update_by_id(self, document_id: str, updates: dict):
        return await self.db[self.collection].update_one(
            {"_id": ObjectId(document_id)}, updates
        )

    async def update_one(self, filters: dict, updates: dict):
        return await self.db[self.collection].update_one(filters, updates)

    async def update_many(self, filters: dict, updates: dict):
        return await self.db[self.collection].update_many(filters, updates)

import json
from typing import Any, Iterable

from bson import ObjectId
from pymongo.results import (
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
)

from infrastructure.managers.kafka import KafkaManager
from infrastructure.managers.mongo_manager import Manager
from infrastructure.repositories.interfaces import IBrokerRepository, IRepository


class BaseRepository(Manager, IRepository):
    """Mongodb base repository with database operations"""

    collection: str

    async def insert_one(self, document: dict) -> InsertOneResult:
        return await self.db[self.collection].insert_one(document)

    async def insert_many(self, documents: Iterable[dict]) -> InsertManyResult:
        return await self.db[self.collection].insert_many(documents)

    async def get_by_id(self, document_id: str, fields: dict) -> dict:
        return await self.db[self.collection].find_one(
            {"_id": ObjectId(document_id)}, fields
        )

    async def get_one(self, filters: dict, fields: dict) -> dict:
        return await self.db[self.collection].find_one(filters, fields)

    async def filter(self, filters: dict, fields: dict) -> list[dict]:
        return await self.db[self.collection].find(filters, fields).to_list(length=None)

    async def get_all(self, fields: dict) -> list[dict]:
        return await self.db[self.collection].find({}, fields).to_list(length=None)

    async def delete_by_id(self, document_id: str) -> DeleteResult:
        return await self.db[self.collection].delete_one({"_id": ObjectId(document_id)})

    async def delete_one(self, filters: dict) -> DeleteResult:
        return await self.db[self.collection].delete_one(filters)

    async def delete_many(self, filters: dict) -> DeleteResult:
        return await self.db[self.collection].delete_many(filters)

    async def update_by_id(self, document_id: str, updates: dict) -> UpdateResult:
        return await self.db[self.collection].update_one(
            {"_id": ObjectId(document_id)}, updates
        )

    async def update_one(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.db[self.collection].update_one(filters, updates)

    async def update_many(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.db[self.collection].update_many(filters, updates)


class BaseBrokerRepository(KafkaManager, IBrokerRepository):
    """Base repository for brokers"""

    topic: str

    async def send(self, value: Any, *args, **kwargs):
        return await self.client.send(
            self.topic, json.dumps(value).encode("utf8"), *args, **kwargs
        )

    async def send_and_wait(self, value: Any, *args, **kwargs):
        return await self.client.send_and_wait(self.topic, value, *args, **kwargs)

    async def send_batch(self, batch: Any, partition: int):
        return await self.client.send_batch(batch, self.topic, partition=partition)

from typing import Iterable

from interfaces.database import IRepository
from interfaces.service import IService


class BaseService(IService):
    """Mongodb base service"""

    repository: IRepository

    async def insert_one(self, document: dict):
        return await self.repository.insert_one(document)

    async def insert_many(self, documents: Iterable[dict]):
        return await self.repository.insert_many(documents)

    async def get_by_id(self, document_id: str):
        return await self.repository.get_by_id(document_id)

    async def get_one(self, filters: dict):
        return await self.repository.get_one(filters)

    async def filter(self, filters: dict):
        return await self.repository.filter(filters)

    async def get_all(self):
        return await self.repository.get_all()

    async def delete_by_id(self, document_id: str):
        return await self.repository.delete_by_id(document_id)

    async def delete_one(self, filters: dict):
        return await self.repository.delete_one(filters)

    async def delete_many(self, filters: dict):
        return await self.repository.delete_many(filters)

    async def update_by_id(self, document_id: str, updates: dict):
        return await self.repository.update_by_id(document_id, updates)

    async def update_one(self, filters: dict, updates: dict):
        return await self.repository.update_one(filters, updates)

    async def update_many(self, filters: dict, updates: dict):
        return await self.repository.update_many(filters, updates)

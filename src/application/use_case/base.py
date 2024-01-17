from typing import Iterable

from pymongo.results import (
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
)

from application.use_case.interfaces import IUseCase
from infrastructure.repositories.interface import IRepository


class BaseUseCase(IUseCase):
    """Base use case"""

    repository: IRepository
    fields: dict

    async def insert_one(self, document: dict) -> InsertOneResult:
        return await self.repository.insert_one(document)

    async def insert_many(self, documents: Iterable[dict]) -> InsertManyResult:
        return await self.repository.insert_many(documents)

    async def get_by_id(self, document_id: str) -> dict:
        return await self.repository.get_by_id(document_id, self.fields)

    async def get_one(self, filters: dict) -> dict:
        return await self.repository.get_one(filters, self.fields)

    async def get_by_filters(self, filters: dict) -> list[dict]:
        return await self.repository.filter(filters, self.fields)

    async def get_all(self) -> list[dict]:
        return await self.repository.get_all(self.fields)

    async def update_by_id(self, document_id: str, updates: dict) -> UpdateResult:
        return await self.repository.update_by_id(document_id, updates)

    async def update_one(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.repository.update_one(filters, updates)

    async def update_many(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.repository.update_many(filters, updates)

    async def delete_by_id(self, document_id: str) -> DeleteResult:
        return await self.repository.delete_by_id(document_id)

    async def delete_one(self, filters: dict) -> DeleteResult:
        return await self.repository.delete_one(filters)

    async def delete_many(self, filters: dict) -> DeleteResult:
        return await self.repository.delete_many(filters)

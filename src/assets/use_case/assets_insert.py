from typing import Iterable

from pymongo.results import InsertManyResult, InsertOneResult

from assets.domain.use_case.insert import IInsertUseCase
from common.infrastructure.repositories.assets import AssetRepository


class AssetInsertUseCase(IInsertUseCase):
    """Asset insert use case"""

    repository = AssetRepository()

    async def insert_one(self, document: dict) -> InsertOneResult:
        return await self.repository.insert_one(document)

    async def insert_many(self, documents: Iterable[dict]) -> InsertManyResult:
        return await self.repository.insert_many(documents)

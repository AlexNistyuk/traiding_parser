from pymongo.results import UpdateResult

from common.domain.repository import IRepository
from common.domain.use_case.update import IUpdateUseCase


class BaseUpdateUseCase(IUpdateUseCase):
    """Base update use case"""

    repository: IRepository

    async def update_by_id(self, document_id: str, updates: dict) -> UpdateResult:
        return await self.repository.update_by_id(document_id, updates)

    async def update_one(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.repository.update_one(filters, updates)

    async def update_many(self, filters: dict, updates: dict) -> UpdateResult:
        return await self.repository.update_many(filters, updates)

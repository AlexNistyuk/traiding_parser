from pymongo.results import DeleteResult

from common.domain.repository import IRepository
from common.domain.use_case.delete import IDeleteUseCase


class BaseDeleteUseCase(IDeleteUseCase):
    """Base delete use case"""

    repository: IRepository

    async def delete_by_id(self, document_id: str) -> DeleteResult:
        return await self.repository.delete_by_id(document_id)

    async def delete_one(self, filters: dict) -> DeleteResult:
        return await self.repository.delete_one(filters)

    async def delete_many(self, filters: dict) -> DeleteResult:
        return await self.repository.delete_many(filters)

from common.domain.repository import IRepository
from common.domain.use_case.get import IGetUseCase


class BaseGetUseCase(IGetUseCase):
    """Base get use case"""

    repository: IRepository
    fields: dict

    async def get_by_id(self, document_id: str) -> dict:
        return await self.repository.get_by_id(document_id, self.fields)

    async def get_one(self, filters: dict) -> dict:
        return await self.repository.get_one(filters, self.fields)

    async def get_by_filters(self, filters: dict) -> list[dict]:
        return await self.repository.filter(filters, self.fields)

    async def get_all(self) -> list[dict]:
        return await self.repository.get_all(self.fields)

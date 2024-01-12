from repositories.assets import AssetRepository
from services.base import BaseService


class AnalyticsService(BaseService):
    repository = AssetRepository()
    fields = {}

    async def get_group_by_assets(self) -> dict:
        return await self.repository.get_group_by_assets()

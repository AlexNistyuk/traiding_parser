from repositories.assets import AssetRepository
from services.base import BaseService


class AssetService(BaseService):
    repository = AssetRepository()

    async def get_group_by_assets(self):
        return await self.repository.get_group_by_assets()

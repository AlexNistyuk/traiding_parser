from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base import BaseUseCase


class AnalyticsUseCase(BaseUseCase):
    """Analytics use case"""

    repository = AssetRepository()
    fields = {}

    async def get_group_by_assets(self) -> dict:
        return await self.repository.get_group_by_assets()
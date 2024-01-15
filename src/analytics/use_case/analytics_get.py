from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base_get import BaseGetUseCase


class AnalyticsGetUseCase(BaseGetUseCase):
    """Analytics get use case"""

    repository = AssetRepository()
    fields = {}

    async def get_group_by_assets(self) -> dict:
        return await self.repository.get_group_by_assets()

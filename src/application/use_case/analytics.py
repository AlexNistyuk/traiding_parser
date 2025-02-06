from application.use_case.base import BaseUseCase
from infrastructure.repositories.assets import AssetRepository


class AnalyticsUseCase(BaseUseCase):
    """Analytics use case"""

    repository = AssetRepository()
    fields = {}

    async def get_group_by_assets(self) -> dict:
        return await self.repository.get_group_by_assets()

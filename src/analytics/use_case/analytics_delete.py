from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base_delete import BaseDeleteUseCase


class AnalyticsDeleteUseCase(BaseDeleteUseCase):
    """Analytics delete use case"""

    repository = AssetRepository()

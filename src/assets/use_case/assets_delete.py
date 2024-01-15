from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base_delete import BaseDeleteUseCase


class AssetDeleteUseCase(BaseDeleteUseCase):
    """Asset delete use case"""

    repository = AssetRepository()

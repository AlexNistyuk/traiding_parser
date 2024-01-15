from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base_update import BaseUpdateUseCase


class AssetUpdateUseCase(BaseUpdateUseCase):
    """Asset update use case"""

    repository = AssetRepository()

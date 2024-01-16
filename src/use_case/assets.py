from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base import BaseUseCase


class AssetUseCase(BaseUseCase):
    """Asset use case"""

    repository = AssetRepository()
    fields = {"_id": True, "symbol": True, "best_bid_price": True, "time": True}

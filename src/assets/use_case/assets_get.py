from common.infrastructure.repositories.assets import AssetRepository
from common.use_case.base_get import BaseGetUseCase


class AssetGetUseCase(BaseGetUseCase):
    """Asset get use case"""

    repository = AssetRepository()
    fields = {"_id": True, "symbol": True, "best_bid_price": True, "time": True}

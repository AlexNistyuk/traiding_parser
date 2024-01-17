from common.repositories.assets import AssetRepository
from common.services.base import BaseUseCase


class AssetUseCase(BaseUseCase):
    """Asset use case"""

    repository = AssetRepository()
    fields = {"_id": True, "symbol": True, "best_bid_price": True, "time": True}

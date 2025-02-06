from application.use_case.base import BaseUseCase
from infrastructure.repositories.assets import AssetRepository


class AssetUseCase(BaseUseCase):
    """Asset use case"""

    repository = AssetRepository()
    fields = {"_id": True, "symbol": True, "best_bid_price": True, "time": True}

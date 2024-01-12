from repositories.assets import AssetRepository
from services.base import BaseService


class AssetService(BaseService):
    repository = AssetRepository()
    fields = {"_id": True, "symbol": True, "best_bid_price": True, "time": True}

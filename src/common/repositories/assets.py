from common.repositories.base import BaseRepository
from infrastructure.config import get_settings


class AssetRepository(BaseRepository):
    collection = get_settings().assets_collection

    async def get_group_by_assets(self) -> dict:
        return (
            await self.db[self.collection]
            .aggregate(
                [
                    {
                        "$group": {
                            "_id": "$symbol",
                            "price_change": {"$push": "$price_change"},
                            "price_change_percent": {"$push": "$price_change_percent"},
                            "current_close_price": {"$push": "$current_close_price"},
                            "previous_close_price": {"$push": "$previous_close_price"},
                            "open_price": {"$push": "$open_price"},
                            "best_bid_price": {"$push": "$best_bid_price"},
                            "high_price": {"$push": "$high_price"},
                            "low_price": {"$push": "$low_price"},
                            "time": {"$push": "$time"},
                        }
                    }
                ]
            )
            .to_list(length=None)
        )[0]

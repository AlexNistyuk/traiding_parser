from config import get_settings
from repositories.base import BaseRepository


class AssetRepository(BaseRepository):
    collection = get_settings().assets_collection

    async def get_group_by_assets(self):
        return (
            await self.db[self.collection]
            .aggregate([{"$group": {"_id": "$symbol", "values": {"$push": "$price"}}}])
            .to_list(length=None)
        )

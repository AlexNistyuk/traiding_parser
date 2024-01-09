from config import get_settings
from repositories.base import BaseRepository


class AssetRepository(BaseRepository):
    collection = get_settings().mongodb_collection

from motor import motor_asyncio

from src.config import MONGODB_COLLECTION, MONGODB_DATABASE, MONGODB_URL

_client = motor_asyncio.AsyncIOMotorClient(MONGODB_URL, uuidRepresentation="standard")
_db = _client[MONGODB_DATABASE]
db_collection = _db[MONGODB_COLLECTION]

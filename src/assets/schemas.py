import datetime

from bson import ObjectId
from pydantic import BaseModel, Field


class AssetCreate(BaseModel):
    symbol: str
    price_change: float
    price_change_percent: float
    current_close_price: float
    previous_close_price: float
    open_price: float
    best_bid_price: float
    high_price: float
    low_price: float
    time: int = int(datetime.datetime.now(tz=datetime.timezone.utc).timestamp())


class PyObjectId(ObjectId):
    """Custom type for reading MongoDB ids"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, *args):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid object_id")
        return value


class AssetGet(AssetCreate):
    id: PyObjectId = Field(default_factory=PyObjectId, validation_alias="_id")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class AssetHistory(BaseModel):
    symbol: str = Field(validation_alias="_id")
    price_change: list
    price_change_percent: list
    current_close_price: list
    previous_close_price: list
    open_price: list
    best_bid_price: list
    high_price: list
    low_price: list
    time: list

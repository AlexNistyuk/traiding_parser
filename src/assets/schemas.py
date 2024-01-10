from bson import ObjectId
from pydantic import BaseModel, Field


class AssetCreate(BaseModel):
    symbol: str
    price: float


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
    values: list

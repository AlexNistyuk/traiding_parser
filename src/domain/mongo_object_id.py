from typing import Any

from bson import ObjectId
from pydantic_core import core_schema


class MongoObjectId(ObjectId):
    """Custom type for reading MongoDB ids"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: ObjectId, *args):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid object_id")
        return str(value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(cls.validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                cls.serialize
            ),
        )

    @staticmethod
    def serialize(value: ObjectId) -> str:
        return str(value)

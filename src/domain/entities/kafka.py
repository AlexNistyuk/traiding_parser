from bson import Decimal128
from pydantic import BaseModel, Field, field_validator


class KafkaDTO(BaseModel):
    symbol: str = Field(
        alias="symbol",
        title="symbol",
        description="Asset name",
        examples=["ETHBTC", "BNBBTC"],
        min_length=2,
        max_length=30,
        repr=True,
        validation_alias="symbol",
        serialization_alias="symbol",
    )
    best_bid_price: str = Field(
        default="0",
        alias="best_bid_price",
        serialization_alias="best_bid_price",
        validation_alias="best_bid_price",
        title="best_bid_price",
        description="current best bid price",
        repr=True,
        validate_default=True,
        examples=["12.54", "-1.049"],
    )
    price_change_percent: int = Field(
        default=0,
        alias="price_change_percent",
        serialization_alias="price_change_percent",
        validation_alias="price_change_percent",
        title="price_change_percent",
        description="price change percent",
        repr=True,
        validate_default=True,
        examples=[-15, 12],
    )

    @field_validator("best_bid_price", mode="before")
    @staticmethod
    def convert_to_str(field_value: Decimal128) -> str:
        return str(field_value.to_decimal())

    @field_validator("price_change_percent", mode="before")
    @staticmethod
    def convert_to_int(field_value: Decimal128) -> int:
        return int(field_value.to_decimal())

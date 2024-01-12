import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from config import get_settings
from utils.mongo import PyObjectId

settings = get_settings()


class AnalyticsGet(BaseModel):
    id: PyObjectId = Field(
        default_factory=PyObjectId,
        alias="_id",
        validation_alias="_id",
        serialization_alias="_id",
        title="id",
        description="ObjectId field",
        examples=["532523sdf3", "123gtrgrt4"],
    )
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
    price_change: Decimal = Field(
        default=0,
        alias="price_change",
        serialization_alias="price_change",
        validation_alias="price_change",
        title="price_change",
        description="difference between current price and previous",
        repr=True,
        validate_default=True,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    price_change_percent: Decimal = Field(
        default=0,
        alias="price_change_percent",
        serialization_alias="price_change_percent",
        validation_alias="price_change_percent",
        title="price_change_percent",
        description="difference between current price and previous in percents",
        repr=True,
        validate_default=True,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    current_close_price: Decimal = Field(
        default=0,
        alias="current_close_price",
        serialization_alias="current_close_price",
        validation_alias="current_close_price",
        title="current_close_price",
        description="current day's close price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    previous_close_price: Decimal = Field(
        default=0,
        alias="previous_close_price",
        serialization_alias="previous_close_price",
        validation_alias="previous_close_price",
        title="previous_close_price",
        description="previous day's close price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    open_price: Decimal = Field(
        default=0,
        alias="open_price",
        serialization_alias="open_price",
        validation_alias="open_price",
        title="open_price",
        description="current day's open price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    best_bid_price: Decimal = Field(
        default=0,
        alias="best_bid_price",
        serialization_alias="best_bid_price",
        validation_alias="best_bid_price",
        title="best_bid_price",
        description="current best bid price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    high_price: Decimal = Field(
        default=0,
        alias="high_price",
        serialization_alias="high_price",
        validation_alias="high_price",
        title="high_price",
        description="current day's high price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    low_price: Decimal = Field(
        default=0,
        alias="low_price",
        serialization_alias="low_price",
        validation_alias="low_price",
        title="low_price",
        description="current day's low price",
        repr=True,
        validate_default=True,
        ge=0,
        decimal_places=settings.decimal_places,
        examples=[Decimal(12.54), Decimal(54.341)],
        max_digits=settings.decimal_max_digits,
    )
    time: int = Field(
        default=int(datetime.datetime.now(tz=datetime.timezone.utc).timestamp()),
        alias="time",
        serialization_alias="time",
        validation_alias="time",
        title="time",
        description="record time",
        repr=True,
        validate_default=True,
        gt=0,
        examples=[1789213123123123, 92838287172381273],
    )

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}


class AnalyticsHistory(BaseModel):
    symbol: str = Field(
        alias="_id",
        title="symbol",
        description="Asset name",
        examples=["ETHBTC", "BNBBTC"],
        min_length=2,
        max_length=10,
        repr=True,
        validation_alias="_id",
        serialization_alias="_id",
    )
    price_change: list = Field(
        default=[0],
        alias="price_change",
        serialization_alias="price_change",
        validation_alias="price_change",
        title="price_change",
        description="list of difference between current price and previous",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    price_change_percent: list = Field(
        default=[0],
        alias="price_change_percent",
        serialization_alias="price_change_percent",
        validation_alias="price_change_percent",
        title="price_change_percent",
        description="list of difference between current prices and previous in percents",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    current_close_price: list = Field(
        default=[0],
        alias="current_close_price",
        serialization_alias="current_close_price",
        validation_alias="current_close_price",
        title="current_close_price",
        description="list of current day's close prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    previous_close_price: list = Field(
        default=[0],
        alias="previous_close_price",
        serialization_alias="previous_close_price",
        validation_alias="previous_close_price",
        title="previous_close_price",
        description="list of previous day's close prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    open_price: list = Field(
        default=[0],
        alias="open_price",
        serialization_alias="open_price",
        validation_alias="open_price",
        title="open_price",
        description="list of current day's open prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    best_bid_price: list = Field(
        default=[0],
        alias="best_bid_price",
        serialization_alias="best_bid_price",
        validation_alias="best_bid_price",
        title="best_bid_price",
        description="list of current best bid prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    high_price: list = Field(
        default=[0],
        alias="high_price",
        serialization_alias="high_price",
        validation_alias="high_price",
        title="high_price",
        description="list of current day's high prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    low_price: list = Field(
        default=[0],
        alias="low_price",
        serialization_alias="low_price",
        validation_alias="low_price",
        title="low_price",
        description="list of current day's low prices",
        repr=True,
        validate_default=True,
        examples=[[12.0, 54.341]],
    )
    time: int = Field(
        default=int(datetime.datetime.now(tz=datetime.timezone.utc).timestamp()),
        alias="time",
        serialization_alias="time",
        validation_alias="time",
        title="time",
        description="list of records time",
        repr=True,
        validate_default=True,
        examples=[[1789213123123123, 92838287172381273]],
    )

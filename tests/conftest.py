import faker
import pytest
from fastapi.testclient import TestClient
from mongomock_motor import AsyncMongoMockClient

from domain.entities.assets import AssetCreateDTO
from infrastructure.config import get_settings
from main import app

client = TestClient(app=app)
settings = get_settings()


@pytest.fixture()
async def fill_assets_collection(monkeypatch):
    mongo_client = AsyncMongoMockClient()
    db = mongo_client.get_database(name=settings.mongodb_database)

    collection = db.get_collection(name=settings.assets_collection)

    monkeypatch.setattr("infrastructure.managers.mongo_manager.Manager.db", db)

    documents = [AssetCreateDTO(**AssetFactory.build()).model_dump() for _ in range(10)]

    await collection.insert_many(documents)


class AssetFactory:
    fake = faker.Faker()

    @classmethod
    def __get_decimal(cls):
        return str(
            cls.fake.pydecimal(
                left_digits=settings.decimal_max_digits - settings.decimal_places,
                right_digits=settings.decimal_places,
                min_value=0.01,
            )
        )

    @classmethod
    def build(cls):
        return {
            "symbol": cls.fake.name(),
            "price_change": cls.__get_decimal(),
            "price_change_percent": cls.__get_decimal(),
            "current_close_price": cls.__get_decimal(),
            "previous_close_price": cls.__get_decimal(),
            "open_price": cls.__get_decimal(),
            "best_bid_price": cls.__get_decimal(),
            "high_price": cls.__get_decimal(),
            "low_price": cls.__get_decimal(),
            "time": cls.fake.pyint(),
        }

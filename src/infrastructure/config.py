import os
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = os.path.join(BASE_DIR.parent.parent, ".env")


class Settings(BaseSettings):
    web_port: int
    web_host: str
    web_scheme: str
    web_container_host: str
    mongodb_url: str
    mongodb_database: str
    assets_collection: str
    redis_host: str
    redis_port: int
    celery_beat_time: int
    celery_queue: str
    decimal_places: int
    decimal_max_digits: int
    binance_api_request_timeout: int
    kafka_host: str
    kafka_port: int
    kafka_binance_topic: str
    default_network: str
    coins_update_endpoint: str

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH)


@lru_cache
def get_settings():
    return Settings()

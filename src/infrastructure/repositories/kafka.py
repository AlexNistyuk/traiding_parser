from infrastructure.config import get_settings
from infrastructure.repositories.base import BaseBrokerRepository


class KafkaBinanceRepository(BaseBrokerRepository):
    topic: str = get_settings().kafka_binance_topic

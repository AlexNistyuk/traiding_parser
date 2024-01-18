from application.use_case.base import BaseBrokerUseCase
from infrastructure.repositories.kafka import KafkaBinanceRepository


class KafkaBinanceUseCase(BaseBrokerUseCase):
    """Kafka use case"""

    repository = KafkaBinanceRepository()

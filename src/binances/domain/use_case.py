from abc import ABC, abstractmethod


class IBinanceUseCase(ABC):
    @abstractmethod
    async def get_tickers_info(self, *args, **kwargs):
        raise NotImplementedError

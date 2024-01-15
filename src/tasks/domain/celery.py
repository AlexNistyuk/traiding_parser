from abc import ABC, abstractmethod


class ICeleryUseCase(ABC):
    @abstractmethod
    async def get_data_and_send(self, *args, **kwargs):
        raise NotImplementedError

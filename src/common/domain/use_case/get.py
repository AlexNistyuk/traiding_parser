from abc import ABC, abstractmethod


class IGetUseCase(ABC):
    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_filters(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[dict]:
        raise NotImplementedError

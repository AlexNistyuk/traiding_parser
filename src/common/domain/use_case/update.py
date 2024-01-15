from abc import ABC, abstractmethod


class IUpdateUseCase(ABC):
    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_many(self, *args, **kwargs):
        raise NotImplementedError

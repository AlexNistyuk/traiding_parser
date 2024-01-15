from abc import ABC, abstractmethod


class IInsertUseCase(ABC):
    @abstractmethod
    async def insert_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def insert_many(self, *args, **kwargs):
        raise NotImplementedError

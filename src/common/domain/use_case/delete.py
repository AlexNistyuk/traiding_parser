from abc import ABC, abstractmethod


class IDeleteUseCase(ABC):
    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, *args, **kwargs):
        raise NotImplementedError

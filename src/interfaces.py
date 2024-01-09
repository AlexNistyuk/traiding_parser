from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def insert_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def insert_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def filter(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplementedError


class IService(ABC):
    @abstractmethod
    async def get_all_tickers(self, *args, **kwargs):
        raise NotImplementedError

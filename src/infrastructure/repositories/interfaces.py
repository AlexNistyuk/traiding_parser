from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    async def insert_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def insert_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def filter(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_many(self, filters: dict, updates: dict):
        raise NotImplementedError


class IBrokerRepository(ABC):
    @abstractmethod
    async def send(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def send_and_wait(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def send_batch(self, *args, **kwargs):
        raise NotImplementedError

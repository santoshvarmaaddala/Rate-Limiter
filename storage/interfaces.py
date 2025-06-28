from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def get(self, key: str) -> str:
        pass

    @abstractmethod
    def set(self, key: str, value: str, ex: int = None) -> None:
        pass

    @abstractmethod
    def increment(self, key: str) -> int:
        pass

    @abstractmethod
    def expire(self, key: str, ttl: int) -> None:
        pass
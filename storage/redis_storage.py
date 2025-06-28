import redis
from storage.interfaces import Storage

class RedisStorage(Storage):
    def __init__(self, host="redis", port=6379, db=0) -> None:
        self.client = redis.Redis(
            host=host,
            port=port,
            db= 0,
            decode_responses=True
        )

    def get(self, key: str) -> str:
        value = self.client.get(key)
        return value
    
    def set(self, key: str, value: str, ex: int = None) -> None:
        self.client.set(name=key, value=value, ex=ex)

    def increment(self, key: str) -> int:
        return self.client.incr(name=key)
    
    def expire(self, key: str, ttl: int) -> None:
        self.client.expire(name=key, time=ttl)
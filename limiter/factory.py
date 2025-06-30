from storage.redis_storage import RedisStorage
from limiter.token_bucket import TokenBucketLimiter
from limiter.interfaces import RateLimiter


class LimiterFactory:

    @staticmethod
    def create_limiter() -> RateLimiter:
        storage = RedisStorage()

        limiter = TokenBucketLimiter(
            storage = storage,
            max_tokens = 5,
            refill_rate_per_sec = 1
        )

        return limiter
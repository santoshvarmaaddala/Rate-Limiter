from limiter.interfaces import RateLimiter
from storage.interfaces import Storage
import time

class TokenBucketLimiter(RateLimiter):
    def __init__(self, storage: Storage, max_tokens: int, refill_rate_per_sec: float) -> None:
        self.storage = storage
        self.max_tokens = max_tokens
        self.refill_rate_per_sec = refill_rate_per_sec

    def allow_request(self, identifier: str) -> bool:
        current_time = time.time()

        token_key = f"token_bucket:{identifier}:tokens"
        timestamp_key = f"token_bucket:{identifier}:last_refill"

        # Get current token count
        tokens = self.storage.get(token_key)
        tokens = float(tokens) if tokens else self.max_tokens

        # Get last refill time
        last_refill = self.storage.get(timestamp_key)
        last_refill = float(last_refill) if last_refill else current_time

        # Calculate how many tokens to add
        elpased = current_time - last_refill
        refill = elpased * self.refill_rate_per_sec
        tokens = min(tokens + refill, self.max_tokens)

        # If tokens available, allow and decrement
        if tokens >= 1:
            tokens -= 1
            allowed = True
        else:
            allowed = False

        self.storage.set(token_key, str(tokens))
        self.storage.set(timestamp_key, str(current_time))

        return allowed
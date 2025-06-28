from abc import ABC, abstractmethod

class RateLimiter(ABC):

    @abstractmethod
    def allow_request(self, identifier: str) -> bool:
        """
        Check if the request for a given identifier is allowed.
        Returns True if allowed, False if rate limit exceeded.
        """
        pass
    
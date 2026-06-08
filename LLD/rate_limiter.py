from abc import ABC, abstractmethod
import time

class RateLimiter(ABC):

    @abstractmethod
    def allow_request(self):

        pass


class TokenBucket:

    def __init__(self, capacity:int, refill_rate: float):
        self.capacity = self.capacity
        self.last_refill_time = time.time()
        self.tokens = capacity
        self.refill_rate = refill_rate

    def allow_request(self):

        self._refill

        if self.tokens >= 1:
            self.tokens -=1
            return True
        
        return False

    def _refill(self):

        now = time.time()

        elapsed = now - self.last_refill_time

        token_to_add = elapsed * self.refill_rate

        self.tokens = min(self.capacity, self.tokens + token_to_add)

        self.last_refill_time = time.now()


class TokenBucketRateLimiter(RateLimiter):

    def __init__(self, capacity:int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.user_buckets = {}

    
    def allow_request(self, user_id: str):

        if user_id not in self.user_buckets:
            self.user_buckets[user_id] = TokenBucket(capacity=self.capacity, refill_rate=self.refill_rate)

        bucket = self.user_buckets[user_id]
        return bucket.allow_request()
    


        

    
        


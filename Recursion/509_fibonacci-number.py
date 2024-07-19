from functools import lru_cache # This increases your execution speed and reduces  execution time

class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        elif n>1:
            return self.fib(n-1) + self.fib( n-2)
        

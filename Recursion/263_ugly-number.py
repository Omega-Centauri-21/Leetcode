class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False

        for ele in [2, 3, 5]:
            while n % ele == 0:
                n //= ele

        return n == 1

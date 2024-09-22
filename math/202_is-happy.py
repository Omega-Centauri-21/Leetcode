class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum([x**2 for x in map(int, str(n))])

        return n == 1

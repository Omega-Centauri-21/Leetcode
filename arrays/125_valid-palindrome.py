class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        r = re.compile("[^a-z0-9]")
        x = r.sub("", s.lower().replace(" ",""))
        
        return x == x[::-1]

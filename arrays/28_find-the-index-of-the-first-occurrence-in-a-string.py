class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        prefix_len = len(needle)

        if len(haystack) < prefix_len:
            return -1
        
        for i in range(len(haystack) - prefix_len + 1):
            if haystack[i:i + prefix_len] == needle:
                return i

        return -1

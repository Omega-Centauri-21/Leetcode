class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_len = len(strs[0])
        for x in strs[1:]:
            prefix_len = min(prefix_len, len(x))
            while not x.startswith(strs[0][:prefix_len]):
                prefix_len -= 1

        prefix = strs[0][: prefix_len]
        return prefix

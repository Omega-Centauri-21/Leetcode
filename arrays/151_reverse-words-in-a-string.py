class Solution:
    def reverseWords(self, s: str) -> str:
        return (" ".join(s.split()[::-1]))
        # s = s.split()
        # res = []
        # st = ""
        # res.append(" ".join((ele) for ele in s[::-1]))
        # for i in res:
        #     st += i
        # return st

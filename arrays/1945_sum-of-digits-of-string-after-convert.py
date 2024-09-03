import string

class Solution(object):
    def getLucky(self, s, k):
        res = ''.join(str(string.ascii_lowercase.index(ele) + 1) for ele in s)

        for _ in range(k):
            res = str(sum(int(digit) for digit in res))

        return int(res)

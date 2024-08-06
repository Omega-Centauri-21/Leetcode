from collections import Counter
from typing import List

# the best solution in the world!
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        num_di = Counter(nums)
        for ele in num_di:
            if num_di[ele] > 2:
                count += (num_di[ele] - 2)
                for i in range(num_di[ele] - 2):
                    nums.remove(ele)

        return len(nums) - count

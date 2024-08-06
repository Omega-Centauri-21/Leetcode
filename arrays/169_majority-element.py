# both the commented and uncommented code work with good efficiency
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # x = Counter(nums)
        # n = len(nums)

        # for i in x:
        #     if x[i] > (n//2):
        #         return i

        nums.sort()
        return nums[len(nums)//2]

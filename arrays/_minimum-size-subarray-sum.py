class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        curr_sum = 0
        left = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                res = min(res, right - left +1)
                curr_sum -= nums[left]
                left += 1

        return res if res != n + 1 else 0

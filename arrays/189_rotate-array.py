class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        k = k % len(nums)  # In case k is larger than the length of nums
        nums[:] = nums[-k:] + nums[:-k]

        # count = 0
        # while count <= k-1:
        #     temp = nums[-1:]
        #     nums.pop()
        #     temp = temp + nums[:len(nums)]
        #     nums = temp
        #     count += 1
        # # print(nums)

        # k = k % len(nums)  # In case k is larger than the length of nums
        # count = 0
        # while count < k:
        #     temp = nums[-1]
        #     nums.pop()
        #     nums.insert(0, temp)
        #     count += 1

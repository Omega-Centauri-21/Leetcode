class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        j_p = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[j_p] = nums[i]
                j_p += 1
        
        for i in range(count):
            nums[j_p] = 0
            j_p += 1
      

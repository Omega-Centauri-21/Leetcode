class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[0:m] + nums2[0:n] 
        temp.sort()

        for i in range(len(temp)):
            nums1[i] = temp[i]

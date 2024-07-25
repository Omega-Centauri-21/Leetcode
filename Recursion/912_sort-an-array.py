class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(array):
            if len(array) <= 1:
                return array

            mid = len(array) //2
            left_half = array[:mid]
            right_half = array[mid:]

            # Recursive call
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)

            return merge(left_half, right_half)

        def merge(left, right):
            new = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1

            while i < len(left):
                new.append(left[i])
                i += 1

            while j < len(right):
                new.append(right[j])
                j += 1

            return new
        return merge_sort(nums)

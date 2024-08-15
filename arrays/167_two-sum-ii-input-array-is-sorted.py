class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        num_to_index = {}

        for i, num in enumerate(numbers):

            complement = target - num
     
            if complement in num_to_index:

                return [num_to_index[complement] + 1, i + 1]

            num_to_index[num] = i
        return []
            

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# O(n) Solution else you get a 'Time Exceeded' Error
       visited = {}
       for i in range(len(nums)):
           if nums[i] in visited:
               j = visited[nums[i]]
               if abs(i-j) <= k:
                   return True
           visited[nums[i]] = i
           continue 
           
       return False

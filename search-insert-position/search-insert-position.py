class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)
        
        
        
        
# loop
# if there is a value, return index
# if the value is smaller, just pass, but greater than target, return the index
# if there are not a value greater than target, return the len(nums)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k = n
        
        while n > 0 and nums[n-1] >= nums[n]:
            n -= 1
        
        i = n
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
        
        if n > 0:
            k = n - 1
            n -= 1
            while nums[k] <= nums[n]:
                k += 1
            nums[k], nums[n] = nums[n], nums[k]
            
        
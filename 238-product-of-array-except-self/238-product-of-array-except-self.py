class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr1 = [0]*length
        arr2 = [0]*length
        result = [0]*length
        
        arr1[0] = 1
        for i in range(1, len(nums)):
            arr1[i] = nums[i-1] * arr1[i-1]
            
        arr2[length - 1] = 1
        for j in range(len(nums)-2, -1, -1):
            arr2[j] = nums[j+1] * arr2[j+1]
        
        for k in range(len(nums)):
            result[k] = arr1[k] * arr2[k]
            
        return result
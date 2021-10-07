class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in nums:
            nums[abs(i) - 1] *= -1
            
        for j in nums:
            if nums[abs(j) - 1] > 0:
                output.append(abs(j))
                nums[abs(j) - 1] *= -1
                
        return output
        
        
        
#         nums = [4,3,2,7,8,2,3,1]
#               [-4,3,2,-7,8,2,-3,-1]
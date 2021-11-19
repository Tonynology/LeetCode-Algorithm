class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = nums
        
        for i in range(len(output)):
            output[i] = output[i]**2
            
        output.sort()
        
        return output
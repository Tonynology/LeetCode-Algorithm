class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        minValue = 0
        
        for i in nums:
            total += i
            minValue = min(minValue, total)
            
        return -minValue + 1
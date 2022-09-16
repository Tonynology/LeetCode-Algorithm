class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxResult = 0
        
        while start < end:
            boundary = min(height[start], height[end])
            maxResult = max(maxResult, (end - start) * boundary)
            
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
                
        return maxResult
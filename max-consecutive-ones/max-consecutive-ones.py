class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = cnt = 0
        
        for i in range(len(nums)):            
            if nums[i] == 0:
                cnt = 0
                continue
            cnt += 1
            output = max(output, cnt)
            
        return output
        
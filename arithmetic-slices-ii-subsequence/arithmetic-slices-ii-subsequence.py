class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [Counter() for _ in range(n)]
        total = 0
        
        #end
        for i in range(n):
            #start
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
                
        # print(dp)
        return total
    
    # [Counter(), 
    #  Counter({2: 1}), 
    #  Counter({2: 2, 4: 1}), 
    #  Counter({2: 3, 6: 1, 4: 1}), 
    #  Counter({2: 4, 4: 2, 8: 1, 6: 1})]
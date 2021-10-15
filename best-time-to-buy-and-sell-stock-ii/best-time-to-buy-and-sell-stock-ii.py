class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        res = 0
        curr = prices[0]
        
        for i in prices:
            res += max(i - curr, 0)
            curr = i
            
        return res
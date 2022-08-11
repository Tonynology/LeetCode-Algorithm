class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maxProfit = 0
        
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > maxProfit:
                maxProfit = prices[i] - minimum
        
        return maxProfit
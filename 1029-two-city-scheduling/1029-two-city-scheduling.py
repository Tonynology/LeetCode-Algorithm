class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2
        
        costs.sort(key = lambda x: x[0] - x[1])
        total = 0
        
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        
        return total
        
        
        
#         A-B = price of send person to city A
#         1. order by A - B
#         2. calculate first half people as send to city A
#         3. rest of them to city B
#         4. sum
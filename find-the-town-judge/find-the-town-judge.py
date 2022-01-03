class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) < n - 1:
            return -1
        
        inCount = [0] * (n + 1)
        outCount = [0] * (n + 1)
        
        for a, b in trust:
            outCount[a] += 1
            inCount[b] += 1
            
        for i in range(1, n + 1):
            if inCount[i] == n - 1 and outCount[i] == 0:
                return i
        
        return -1
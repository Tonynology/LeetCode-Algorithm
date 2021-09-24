class Solution:
    def tribonacci(self, n: int) -> int:
        F = [0 for _ in range(38)]
        
        F[0] = 0
        F[1] = F[2] = 1
        
        for j in range(3, n+1):
            F[j] = F[j-1] + F[j-2] + F[j-3]
            
        return F[n]
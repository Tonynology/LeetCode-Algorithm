class Solution:
    def numSquares(self, n: int) -> int:
        
        #dfs
        def is_divided_by(n, count):
            
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False
            
        
        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
                        
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count
        
        
# 1,4,9,16,25,36,49,64 

# 1,2,3, 4, 5, 6, 7, 8
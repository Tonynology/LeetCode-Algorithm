class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        todo = n
        bit = 1
        
        while todo:
            n = n ^ bit
            bit = bit << 1
            todo = todo >> 1
            
        return n
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        
        count = 1
        output = count
        
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                output = max(output, count)
            else:
                count = 1
            
        return output
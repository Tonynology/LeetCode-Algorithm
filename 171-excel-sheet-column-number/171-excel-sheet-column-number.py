class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #left to right
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26
            result += (ord(columnTitle[i]) - ord('A') + 1)
        return result
        
        
        
        
        
        #right to left
#         result = 0
        
#         alpha_map = {chr(i + 65) : i + 1 for i in range(26)}
        
#         n = len(columnTitle)
#         for i in range(n):
#             cur_char = columnTitle[n - 1 -i]
#             result += (alpha_map[cur_char] * 26 ** i)
#         return result
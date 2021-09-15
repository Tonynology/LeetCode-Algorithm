class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start, end = 0, len(s)-1
        res1 = ""
        res2 = ""
        
        while start < end:
            if s[start].isalpha() and s[end].isalpha():
                res1 = res1 + s[end]
                res2 = s[start] + res2
                start += 1
                end -= 1
            elif not s[start].isalpha():
                res1 = res1 + s[start]
                start += 1
            elif not s[end].isalpha():
                res2 = s[end] + res2
                end -= 1
        
        output = ""
        if start == end:
            output = res1 + s[start] + res2
        else:
            output = res1 + res2
            
        return output
            
                
class Solution:
    def reverseWords(self, s: str) -> str:
        length = len(s)
        i = 0
        stack = []
        output = ""
        
        while i < length:
            if s[i] == ' ':
                #pop stack and add in output
                while stack:
                    ch = stack.pop()
                    output += ch
                output += ' '
            else:
                #just put char in stack
                stack.append(s[i])
            i += 1
        
        while stack:
            ch = stack.pop()
            output += ch
        
        return output
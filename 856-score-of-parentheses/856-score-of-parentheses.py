class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for x in s:
            if x == "(":
                stack.append(0)
            else:
                b = stack.pop()
                stack[-1] += max(2*b, 1)
            
        return stack.pop()
class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == "+":
                stack.append(v)
            if op == "-":
                stack.append(-v)
            if op == "*":
                stack.append(stack.pop() * v)
            if op == "/":
                stack.append(int(stack.pop() / v))
            
        sign, nums= "+", 0
        it = 0
        stack = []
        
        while it < len(s):
            if s[it].isdigit():
                nums = nums * 10 + int(s[it])
                
            elif s[it] in "+-*/":
                update(sign, nums)
                nums, sign = 0, s[it]
                
            elif s[it] == "(":
                nums, j = self.calculate(s[it + 1 :])
                it += j
                
            elif s[it] == ")":
                update(sign, nums)
                return sum(stack), it+1
                
            it += 1
        
        update(sign, nums)
        return sum(stack)
    
        
        
#         if s[i] == digit
#         if s[i] == + - * /:
#         if s[i] == (:
#         if s[i] == ):
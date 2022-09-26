class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        
        operators = ('+', '-', '*', '/')
        
        for token in tokens:
            if token in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num2 * num1)
                elif token == '/':
                    stack.append(int(num2 / num1))
            else:
                stack.append(token)
        
        return stack.pop()
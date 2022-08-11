class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        
        for i in s:
            if i in dict1.values():
                stack.append(i)
            elif i in dict1.keys():
                if stack == [] or dict1[i] != stack.pop():
                    return False
        
        return stack == []
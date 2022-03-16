class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        poppedIndex = 0
        
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[poppedIndex]:
                stack.pop()
                poppedIndex += 1
                
        return len(stack) == 0
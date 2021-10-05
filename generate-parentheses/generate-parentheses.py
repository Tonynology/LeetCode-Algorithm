class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(res, op, cl, st):
            if len(st) == n * 2:
                res.append(st)
                return
            
            if op < n:
                helper(res, op+1, cl, st+"(")
            if cl < op:  ##이것이 포인트. close가 open보다 커야 괄호가 만들어진다.
                helper(res, op, cl+1, st+")")
                
            
                
        res = []
        helper(res, 0, 0, "")
        return res
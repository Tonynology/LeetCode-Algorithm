class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        ans = []
        last_happenedElement = {c: i for i, c in enumerate(s)}
        
        anchor = j = 0
        for i, c in enumerate(s):
            j = max(j, last_happenedElement[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        
        return ans
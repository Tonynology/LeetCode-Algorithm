class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1 = len(firstList)
        l2 = len(secondList)
        i = j = 0
        output = []
        
        
        while i < l1 and j < l2:
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                output.append([lo, hi])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            
        return output
        
        
# if firstList second element is greater (or equal) than secondList first element, there is a intersection.
# if firstList first element is smaller (or equal) than secondList second element, there is a intersection.
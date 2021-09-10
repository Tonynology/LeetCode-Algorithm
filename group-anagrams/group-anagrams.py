class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}
        
        for i in strs:
            keys = "".join(sorted(i))
            if keys not in dict1:
                dict1[keys] = [i]
            else:
                dict1[keys] += [i]
                
        return dict1.values()
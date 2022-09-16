from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        
        left = right = 0
        res = 0
        
        while right < len(s):
            chars[s[right]] += 1
            
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
            right += 1
        
        return res
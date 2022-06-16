class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        
        def helper(l, r):
            res = ""
            resLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            return res
        
        for i in range(len(s)):
            l, r = i, i
            ans = max(helper(l, r), helper(l, r+1), ans, key=len)
                    # odd length,  even length,  ans,  key=function => len
            
        return ans
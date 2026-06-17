class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0
        d = {}
        ret = 0

        while r < len(s):
            if s[r] in d:
                i = d[s[r]]
                while l <= i:
                    del d[s[l]]
                    l += 1
            
            ret = max(ret, r - l + 1)

            d[s[r]] = r
            r += 1
        
        return ret

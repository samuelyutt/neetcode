class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def devide(s, t):
            if len(t) == 0 or len(s) < len(t) or len(s) % len(t):
                return False
            
            l, r = 0, len(t)

            while r <= len(s):
                if s[l:r] != t:
                    return False
                l += len(t)
                r += len(t)

            return True

        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        ret = ''
        for i in range(1, len(str2) + 1):
            if devide(str1, str1[:i]) and devide(str2, str1[:i]):
                ret = str1[:i]

        return ret

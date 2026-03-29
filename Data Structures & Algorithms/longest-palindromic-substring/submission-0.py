class Solution:
    def longestPalindrome(self, s: str) -> str:

        def is_palindrom(s):
            for i in range(len(s) // 2):
                if s[i] != s[-i-1]:
                    return False
            return True

        l, r = 0, 0
        length = 0
        ret = None
        while l <= r < len(s):
            while r < len(s):
                if is_palindrom(s[l:r + 1]):
                    if (r - l + 1 > length):
                        length = r - l + 1
                        ret = s[l:r + 1]
                r += 1
            l += 1
            r = l + length - 1
        
        return ret
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(i):
            return clean[i].upper() == clean[-1 - i].upper()

        clean = ''
        for c in s:
            if 0 <= (ord(c) - ord('A')) < 26 or 0 <= (ord(c) - ord('a')) < 26 or 0 <= (ord(c) - ord('0')) < 9:
                clean += c
        
        for i in range(len(clean) // 2):
            if not helper(i):
                return False
        
        return True
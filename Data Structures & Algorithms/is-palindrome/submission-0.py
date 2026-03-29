class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for char in s.lower():
            if (0 <= ord(char) - ord('a') < 26) or (0 <= ord(char) - ord('0') < 10):
                tmp += char
        for i in range(len(tmp) // 2):
            if tmp[i] != tmp[-i-1]:
                return False
        
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def compare(l, r, deleted):
            if l >= r:
                return True
            if s[l] == s[r]:
                return compare(l + 1, r - 1, deleted)
            if deleted:
                return False
            return compare(l + 1, r, True) or compare(l, r - 1, True)
        return compare(0, len(s) - 1, False)
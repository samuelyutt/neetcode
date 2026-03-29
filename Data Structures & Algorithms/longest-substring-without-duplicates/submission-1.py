class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abc
        # abcabc
        # cabadcba
        # bdadcba

        hashset = set()
        max_length = 0
        l, r = 0, 0
        while r < len(s):
            new_char = s[r]
            while new_char in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(new_char)
            length = r - l + 1
            max_length = max(max_length, length)
            r += 1

        return max_length




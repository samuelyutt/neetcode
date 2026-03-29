class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABABB 1
        # l
        #  r

        res = 0
        freq = {}
        max_freq = 0
        l, r = 0, 0

        while len(s) - l > res and r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(max_freq, freq[s[r]])

            if r - l + 1 > max_freq + k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res




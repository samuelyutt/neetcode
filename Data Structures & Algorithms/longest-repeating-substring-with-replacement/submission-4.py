class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = r = 0
        ret = 0
        cnt = {}

        while r < len(s):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])

            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1

            ret = max(r - l + 1, ret)

            r += 1

        return ret


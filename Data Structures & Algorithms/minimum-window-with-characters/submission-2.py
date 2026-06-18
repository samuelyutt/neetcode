class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, count = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
            count[c] = 0

        have = 0

        min_len = float('inf')
        ret = ''

        l, r = 0, 0

        while r < len(s):
            c = s[r]

            if c in count:
                count[c] += 1
                if count[c] == need[c]:
                    have += 1

            while have == len(need):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ret = s[l: r + 1]

                if s[l] in count:
                    count[s[l]] -= 1
                    if count[s[l]] < need[s[l]]:
                        have -= 1
                l += 1

            r += 1

        return ret


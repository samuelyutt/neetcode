class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # abcc lecabc
        # abcc lecacabc

        l, r = 0, 0
        remains = 0
        remain_cnt = {} # c -> remain_cnt

        for c in s1:
            remain_cnt[c] = remain_cnt.get(c, 0) + 1
            remains += 1

        while l <= r < len(s2):
            if s2[r] in remain_cnt:
                remain_cnt[s2[r]] -= 1
                remains -= 1

                while remain_cnt[s2[r]] < 0:
                    remain_cnt[s2[l]] += 1
                    remains += 1
                    l += 1

                if remains == 0:
                    return True

                r += 1
            else:
                while l < r:
                    remain_cnt[s2[l]] += 1
                    remains += 1
                    l += 1
                r += 1
                l = r

        return False
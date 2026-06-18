class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = {}
        for c in s1:
            c1[c] = c1.get(c, 0) + 1

        c2 = {}
        have = 0
        l, r = 0, 0

        for _ in range(len(s1)):
            c = s2[r]
            if c in c1:
                c2[c] = c2.get(c, 0) + 1
                if c2[c] == c1[c]:
                    have += 1
            r += 1

        while r < len(s2):
            if have == len(c1):
                return True

            c = s2[r]
            if c in c1:
                c2[c] = c2.get(c, 0) + 1
                if c2[c] == c1[c]:
                    have += 1
            r += 1

            c = s2[l]
            if c in c1:
                c2[c] -= 1
                if c2[c] == c1[c] - 1:
                    have -= 1
            l += 1

        if have == len(c1):
            return True
        return False
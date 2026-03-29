class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # abc bc
        # abbcabc abc
        # aabc abc
        # baabc abc

        cnts = {}
        l, r = 0, 0
        min_len = 1001
        min_str = ''

        for c in t:
            cnts[c] = cnts.get(c, 0) + 1

        while l <= r < len(s):
            if s[r] in cnts :
                cnts[s[r]] -= 1

                while l <= r:
                    fit = True
                    for c in cnts:
                        if cnts[c] > 0:
                            fit = False
                            break
                    if fit:
                        if r - l + 1 < min_len:
                            min_len = r - l + 1
                            min_str = s[l : r + 1]
                            print(min_str)
                        if s[l] in cnts :
                            cnts[s[l]] += 1
                        l += 1
                    else:
                        break

            r += 1

        return min_str

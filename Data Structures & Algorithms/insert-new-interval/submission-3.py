class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        s, e = newInterval

        for a, b in intervals:
            if b < s:
                l.append([a, b])
            elif a > e:
                r.append([a, b])
            else:
                s = min(s, a)
                e = max(e, b)

        return l + [[s, e]] + r
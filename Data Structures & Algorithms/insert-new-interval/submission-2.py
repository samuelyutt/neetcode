class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        s, e = newInterval

        for a, b in intervals:
            if b < newInterval[0]:
                l.append([a, b])
            elif a > newInterval[1]:
                r.append([a, b])
            else:
                s, e = min(s, a), max(e, b)

        return l + [[s, e]] + r
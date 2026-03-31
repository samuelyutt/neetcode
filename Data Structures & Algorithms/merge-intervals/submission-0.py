class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        used = set()
        ret = []
        for i in range(len(intervals)):
            if i in used:
                continue
            l, r = intervals[i][0], intervals[i][1]
            used.add(i)
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] > r:
                    break
                r = max(r, intervals[j][1])
                used.add(j)
            ret.append([l, r])
        return ret
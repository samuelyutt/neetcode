class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        intervals.sort()
        e = intervals[0][0]

        for a, b in intervals:
            if a >= e:
                e = b

            else:
                ret += 1
                e = min(e, b)
        
        return ret
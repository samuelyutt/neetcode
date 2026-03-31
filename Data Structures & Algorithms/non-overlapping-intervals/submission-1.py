class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        used = []
        for interval in intervals:
            if not used or interval[0] >= used[-1][1]:
                # safe to add this interval directly
                used.append(interval)
            else:
                # overlapped
                if used[-1][1] > interval[1]:
                    used.pop()
                    used.append(interval)
        return len(intervals) - len(used)
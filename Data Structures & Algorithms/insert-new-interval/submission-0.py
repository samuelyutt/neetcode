class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lefts, mids, rights = [], [newInterval], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                lefts.append(interval)
            elif interval[0] > newInterval[1]:
                rights.append(interval)
            else:
                mids.append(interval)
        return lefts + [[min([mid[0] for mid in mids]), max([mid[1] for mid in mids])]] + rights
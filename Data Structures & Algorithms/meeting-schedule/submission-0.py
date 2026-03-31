"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = [[interval.start, interval.end] for interval in intervals]
        l.sort()
        cur_max = 0
        for interval in l:
            if interval[0] < cur_max:
                return False
            cur_max = max(cur_max, interval[1])
        return True
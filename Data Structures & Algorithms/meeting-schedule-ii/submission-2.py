"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        l = [[interval.start, interval.end] for interval in intervals]
        l.sort()
        h = [] # [(cur_max, room)]
        rooms = 0
        for interval in l:
            if h and interval[0] >= h[0][0]:
                _, room = heapq.heappop(h)
                heapq.heappush(h, (interval[1], room))
            else:
                rooms += 1
                heapq.heappush(h, (interval[1], rooms))
        return rooms

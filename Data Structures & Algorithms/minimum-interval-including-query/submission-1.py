class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q = [(query, i) for i, query in enumerate(queries)]
        q.sort()
        h = [] # [(length, end)]
        i = 0
        ret = [-1] * len(queries)
        for query, qi in q:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(h, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while h and h[0][1] < query:
                heapq.heappop(h)
            if h:
                ret[qi] = h[0][0]
        return ret
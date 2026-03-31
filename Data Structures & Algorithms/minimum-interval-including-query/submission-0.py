class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = [(itvl[1] - itvl[0] + 1, itvl[0], itvl[1]) for itvl in intervals]
        heapq.heapify(h)
        q = [(query, i) for i, query in enumerate(queries)]
        q.sort()
        ret = [-1] * len(queries)
        while h:
            length, l, r = heapq.heappop(h)
            for query, i in q:
                if ret[i] != -1:
                    continue
                if query < l:
                    continue
                if query > r:
                    break
                ret[i] = length
        return ret
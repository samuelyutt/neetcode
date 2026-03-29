class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # (-dist, i, [x, y])
        for i, p in enumerate(points):
            x, y = p[0], p[1]
            dist = x**2 + y**2
            if len(h) < k or dist < -h[0][0]:
                heapq.heappush(h, (-dist, i, [x, y]))
            if len(h) > k:
                heapq.heappop(h)
        return [[p[0], p[1]] for _, _, p in h]
                
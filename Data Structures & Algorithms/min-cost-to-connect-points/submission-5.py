class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        
        d = defaultdict(list) # point_i -> [(dist, point_j)]
        for i, pi in enumerate(points):
            for j, pj in enumerate(points):
                dist = abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])
                d[i].append((dist, j))
        
        ret = 0
        visited = {0}
        h = []
        for dist, i in d[0]:
            heapq.heappush(h, (dist, i))

        while len(visited) != len(points):
            dist, i = heapq.heappop(h)
            if i in visited:
                continue
            for next_dist, j in d[i]:
                heapq.heappush(h, (next_dist, j))
            ret += dist
            visited.add(i)

        return ret

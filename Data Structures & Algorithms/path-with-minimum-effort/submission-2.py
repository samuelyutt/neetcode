class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        h = [(0, 0, 0)]
        visited = set()

        while h:
            cur, i, j = heapq.heappop(h)
            if (i, j) == (m - 1, n - 1):
                return cur
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not 0 <= x < m or not 0 <= y < n:
                    continue
                if (x, y) in visited:
                    continue
                heapq.heappush(h, (max(cur, abs(heights[i][j] - heights[x][y])), x, y))
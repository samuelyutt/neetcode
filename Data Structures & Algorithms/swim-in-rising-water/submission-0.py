class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h = [(grid[0][0], 0, 0)] # [(level, i, j)]
        ret = 0
        while h:
            level, i, j = heapq.heappop(h)
            ret = max(ret, level)
            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return ret
            grid[i][j] = -1
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if not 0 <= x < len(grid) or not 0 <= y < len(grid[x]):
                    continue
                if grid[x][y] == -1:
                    continue
                heapq.heappush(h, (grid[x][y], x, y))
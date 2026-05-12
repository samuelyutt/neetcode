class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n:
                return 10000001
            if (x, y) == (m - 1, n - 1):
                return grid[x][y]
            if (x, y) not in memo:
                memo[(x, y)] = min(
                    dfs(x + 1, y),
                    dfs(x, y + 1),
                ) + grid[x][y]
            return memo[(x, y)]

        return dfs(0, 0)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        
        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n:
                return 0
            if obstacleGrid[x][y]:
                return 0
            if (x, y) == (m - 1, n - 1):
                return 1
            if (x, y) in memo:
                return memo[(x, y)]
            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
            return memo[(x, y)]

        return dfs(0, 0)
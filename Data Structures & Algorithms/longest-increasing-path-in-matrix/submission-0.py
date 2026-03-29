class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            ret = 0
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if not 0 <= x < len(matrix) or not 0 <= y < len(matrix[x]):
                    continue
                if not matrix[x][y] > matrix[i][j]:
                    continue
                ret = max(dfs(x, y), ret)
            memo[(i, j)] = ret + 1
            return ret + 1

        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ret = max(dfs(i, j), ret)
        return ret
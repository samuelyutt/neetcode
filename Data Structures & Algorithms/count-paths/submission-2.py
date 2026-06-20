class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([0] * n)
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        
        return dp[-1][-1]
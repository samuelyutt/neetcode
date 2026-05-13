class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = []
        for _ in range(n):
            dp.append([0] * n)
        sums = [0]
        s = 0
        for pile in piles:
            s += pile
            sums.append(s)

        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = piles[i]
                elif j - i == 1:
                    dp[i][j] = max(piles[i], piles[j])
                elif j - i == 2:
                    dp[i][j] = piles[i] + piles[j]
                else:
                    s = sums[j + 1] - sums[i]
                    dp[i][j] = max(
                        s - dp[i + 1][j],
                        s - dp[i][j - 1],
                    )

        return dp[0][n - 1] > 0
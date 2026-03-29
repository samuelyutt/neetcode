class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        dp = []
        for _ in range(len(coins) + 1):
            dp.append([0] * (amount + 1))

        for i, coin in enumerate(coins, 1):
            dp[i][0] = 1
            for j in range(1, coin):
                dp[i][j] = dp[i - 1][j]
            for j in range(coin, len(dp[i])):
                dp[i][j] = dp[i][j - coin] + dp[i - 1][j]
        print(dp)

        return dp[-1][-1]
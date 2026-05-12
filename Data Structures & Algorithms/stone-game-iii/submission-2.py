class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n

        for i in range(n - 1, -1, -1):
            score = 0
            for j in range(3):
                if i + j >= n:
                    continue
                score += stoneValue[i + j]
                dp[i] = max(
                    dp[i],
                    score - (dp[i + j + 1] if i + j + 1 < n else 0)
                )

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
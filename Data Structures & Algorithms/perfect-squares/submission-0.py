class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        dp = [10001] * (n + 1)
        next_square_side = 1
        for i in range(len(dp)):
            if i == next_square_side**2:
                squares.append(next_square_side**2)
                next_square_side += 1
                dp[i] = 1
            else:
                val = dp[i]
                for square in squares:
                    val = min(val, dp[i - square] + 1)
                dp[i] = val
        return dp[n]
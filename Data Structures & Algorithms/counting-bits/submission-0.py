class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)
        dp[1] = 1

        x = 1
        k = 0
        for i in range(2, n + 1):
            if x * 2 == i:
                k = 0
                x *= 2
            else:
                k += 1
            dp[i] = 1 + dp[k]

        return dp

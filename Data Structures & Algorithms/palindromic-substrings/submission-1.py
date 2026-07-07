class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = []
        for _ in range(n):
            dp.append([0] * n)

        cnt = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i <= 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    cnt += 1
        
        return cnt

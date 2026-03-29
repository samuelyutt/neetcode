class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [] # dp[i][j] means whether s[i..j] is a palindrom
        for _ in range(len(s)):
            dp.append([False for _ in range(len(s))])

        ret = 0
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i, len(dp[i])):
                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    ret += 1
        return ret
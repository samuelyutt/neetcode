class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            
            ret = 0

            if s[i] != '0' and i < len(s) - 1 and int(s[i:i + 2]) <= 26:
                ret += dfs(i + 2)

            if s[i] != '0':
                ret += dfs(i + 1)

            dp[i] = ret

            return ret

        return dfs(0)
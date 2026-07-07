class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]
            
            ret = dfs(i + 1)

            if i < len(s) - 1 and int(s[i:i + 2]) <= 26:
                ret += dfs(i + 2)

            dp[i] = ret

            return ret

        return dfs(0)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        for i in range(1, len(dp)):
            if s[i] == '1':
                continue
            for j in range(minJump, maxJump + 1):
                if i - j < 0:
                    break
                dp[i] |= dp[i - j]
        return dp[-1]
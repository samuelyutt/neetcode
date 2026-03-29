class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) >= len(dp):
                    continue
                if not dp[i + len(word)]:
                    continue
                if word != s[i: i + len(word)]:
                    continue
                dp[i] = True
                break
        return dp[0]

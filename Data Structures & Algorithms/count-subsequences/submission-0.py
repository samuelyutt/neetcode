class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ret = dfs(i + 1, j)
            if s[i] == t[j]:
                ret += dfs(i + 1, j + 1)
            memo[(i, j)] = ret
            return ret

        return dfs(0, 0)
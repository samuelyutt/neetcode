class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if j == len(p) and i == len(s):
                return True
            elif j == len(p) or i == len(s):
                return False

            if p[j] == '*':
                return False
            if (i, j) in dp:
                return dp[(i, j)]

            if j + 1 < len(p) and p[j + 1] == '*':
                if p[j] == '.' or p[j] == s[i]:
                    ret = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    ret = dfs(i, j + 2)
            elif p[j] == '.' or p[j] == s[i]:
                ret = dfs(i + 1, j + 1)
            else:
                ret = False

            dp[(i, j)] = ret
            return ret

        s += '#'
        p += '#'
        return dfs(0, 0)
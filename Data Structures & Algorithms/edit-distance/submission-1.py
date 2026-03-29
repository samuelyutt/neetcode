class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        if word1 == word2:
            return 0

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                ret = 1 + dfs(i, j + 1) # insert
            elif j >= len(word2):
                ret = 1 + dfs(i + 1, j) # delete
            else:
                if word1[i] == word2[j]:
                    ret = dfs(i + 1, j + 1) # next char
                else:
                    ret = 1 + min(
                        dfs(i + 1, j + 1), # replace
                        dfs(i, j + 1), # insert
                        dfs(i + 1, j), # delete
                    )
            memo[(i, j)] = ret
            return ret

        return dfs(0, 0)
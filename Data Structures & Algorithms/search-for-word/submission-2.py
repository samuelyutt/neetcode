class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])

        def dfs(i, x, y):
            if i == len(word):
                return True

            if (x, y) in visited:
                return False

            if not 0 <= x < m or not 0 <= y < n:
                return False

            if board[x][y] == word[i]:
                visited.add((x, y))
                ret = (
                    dfs(i + 1, x + 1, y) or
                    dfs(i + 1, x - 1, y) or
                    dfs(i + 1, x, y + 1) or
                    dfs(i + 1, x, y - 1)
                )
                visited.remove((x, y))
                return ret
            else:
                return False

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True

        return False

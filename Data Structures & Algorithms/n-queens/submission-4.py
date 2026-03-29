class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        def search(pos, queens, avails):
            if pos not in avails:
                return
            avails.remove(pos)
            queens.add(pos)
            x, y = pos
            for i in range(n):
                avails.discard((x, i))
                avails.discard((i, y))
                avails.discard((x + i, y + i))
                avails.discard((x + i, y - i))
                avails.discard((x - i, y + i))
                avails.discard((x - i, y - i))
            if len(queens) == n:
                # answer found
                board = ['.' * n for _ in range(n)]
                for (i, j) in queens:
                    board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
                ret.append(board)
                return
            elif len(avails) + len(queens) >= n:
                # search in the next col
                for (i, j) in avails:
                    if j == y + 1:
                        search((i, j), queens.copy(), avails.copy())

        for i in range(n):
            # search in the first col
            search((i, 0), set(), {(x, y) for x in range(n) for y in range(n)})

        return ret

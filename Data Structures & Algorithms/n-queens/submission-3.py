class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        def search(pos, queens, avails):
            if pos in avails:
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
                    board = ['.' * n for _ in range(n)]
                    for (i, j) in queens:
                        board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
                    ret.append(board)
                    return
                elif len(avails) + len(queens) >= n:
                    for (i, j) in avails:
                        if j == y + 1:
                            search((i, j), queens.copy(), avails.copy())
                else:
                    return
            else:
                return

        for i in range(n):
            search((i, 0), set(), {(x, y) for x in range(n) for y in range(n)})

        return ret

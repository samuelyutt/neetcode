class Solution:
    def solve(self, board: List[List[str]]) -> None:
        w, h = len(board[0]), len(board)
        q = deque([(i, j) for i in range(h) for j in range(w) if i in [0, h - 1] or j in [0, w - 1]])
        while q:
            x, y = q.popleft()
            if not 0 <= x < h or not 0 <= y < w:
                continue
            if board[x][y] != 'O':
                continue
            board[x][y] = '#'
            q.append((x + 1, y))
            q.append((x - 1, y))
            q.append((x, y + 1))
            q.append((x, y - 1))
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
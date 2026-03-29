class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = []
        for row in board:
            used.append([False for _ in row])
        
        def search(i, j, idx):
            if idx >= len(word):
                return False
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if not used[i][j] and board[i][j] == word[idx]:
                used[i][j] = True
                if idx == len(word) - 1:
                    return True
                else:
                    if search(i - 1, j, idx + 1):
                        return True
                    if search(i + 1, j, idx + 1):
                        return True
                    if search(i, j - 1, idx + 1):
                        return True
                    if search(i, j + 1, idx + 1):
                        return True
                used[i][j] = False
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if search(x, y, 0):
                    return True
        
        return False
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_constraints = [{key: False for key in range(9)} for _ in range(9)]
        col_constraints = [{key: False for key in range(9)} for _ in range(9)]
        square_constraints = {}
        for x in range(3):
            for y in range(3):
                square_constraints[(x, y)] = {key: False for key in range(9)}

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == '.':
                    continue
                num = int(num) - 1

                if row_constraints[i][num]:
                    return False
                if col_constraints[j][num]:
                    return False
                if square_constraints[(i//3, j//3)][num]:
                    return False

                row_constraints[i][num] = True
                col_constraints[j][num] = True
                square_constraints[(i//3, j//3)][num] = True

        return True
                
                
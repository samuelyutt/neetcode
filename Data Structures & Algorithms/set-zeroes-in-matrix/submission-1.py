class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        z_in_first_row, z_in_first_col = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                z_in_first_col = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                z_in_first_row = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if z_in_first_col:
            for i in range(m):
                matrix[i][0] = 0
        if z_in_first_row:
            for j in range(n):
                matrix[0][j] = 0
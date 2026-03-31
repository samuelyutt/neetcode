class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        top, down, left, right = 0, m - 1, 0, n - 1
        ret = []
        i, j = 0, 0
        while len(ret) < m * n:
            ret.append(matrix[i][j])
            if di == 0 and j == right:
                top += 1
                di += 1
            elif di == 1 and i == down:
                right -= 1
                di += 1
            elif di == 2 and j == left:
                down -= 1
                di += 1
            elif di == 3 and i == top:
                left += 1
                di += 1
            di %= 4
            dir = dirs[di]
            i += dir[0]
            j += dir[1]
        return ret
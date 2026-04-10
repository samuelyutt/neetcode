class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.areas = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                area = matrix[i][j]
                area += self.areas.get((i - 1, j), 0)
                area += self.areas.get((i, j - 1), 0)
                area -= self.areas.get((i - 1, j - 1), 0)
                self.areas[(i, j)] = area

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        area = self.areas.get((row2, col2), 0)
        area -= self.areas.get((row1 - 1, col2), 0)
        area -= self.areas.get((row2, col1 - 1), 0)
        area += self.areas.get((row1 - 1, col1 - 1), 0)
        return area

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
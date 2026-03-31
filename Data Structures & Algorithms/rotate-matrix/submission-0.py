class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1], matrix[-j - 1][i] = matrix[-j - 1][i], matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1]

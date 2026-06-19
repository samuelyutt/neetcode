class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        l, r = 0, m
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        x = l

        l, r = 0, n
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[x][mid] > target:
                r = mid - 1
            else:
                l = mid
        y = l

        return matrix[x][y] == target
class Solution:
    def binarySearch(self, nums, target) -> int:
        # 5 -> 5
        # 1 2 -> 3
        # 1 10 23 -> 11
        # 1 9 10 23 -> 11
        l, r = 0, len(nums)
        m = 0
        while l < r:
            if nums[l] > target:
                break
            m = (l + r - 1) // 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                break
        return m

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binarySearch([row[0] for row in matrix], target)
        col = self.binarySearch(matrix[row], target)
        return matrix[row][col] == target
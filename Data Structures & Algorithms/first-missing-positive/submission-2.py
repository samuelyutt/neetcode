class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        one = False
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 1
            elif nums[i] == 1:
                one = True

        if not one:
            return 1

        for i in range(n):
            if nums[i] == -1:
                continue
            if 0 <= abs(nums[i]) - 1 < n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for i in range(1, n):
            if nums[i] > 0:
                return i + 1
        return n + 1
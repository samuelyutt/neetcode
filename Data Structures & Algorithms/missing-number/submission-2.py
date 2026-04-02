class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                idx = nums[i]
            else:
                idx = nums[i] + n + 1
            if 0 <= idx < n:
                nums[idx] = nums[idx] - n - 1
        for i in range(n):
            if nums[i] >= 0:
                return i
        return n
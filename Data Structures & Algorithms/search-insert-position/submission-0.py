class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if target >= nums[m]:
                l = m
            else:
                r = m - 1
        return l + 1 if target > nums[l] else l
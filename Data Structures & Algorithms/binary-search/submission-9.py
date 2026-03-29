class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        m = 0
        while l < r:
            m = (l + r - 1) // 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                break
        return m if nums[m] == target else -1
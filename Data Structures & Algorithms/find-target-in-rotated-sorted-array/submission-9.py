class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r + 1) // 2

            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1

        return l if target == nums[l] else -1
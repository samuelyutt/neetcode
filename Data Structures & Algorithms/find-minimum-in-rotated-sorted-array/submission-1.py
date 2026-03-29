class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1
        # 2 1
        # 3 1 2
        # 3 4 1 2
        # 1 2 3 4
        # 4 1 2 3

        l, r = 0, len(nums) - 1
        while r - l > 1:
            m = (l + r + 1) // 2
            if nums[l] > nums[m]:
                l, r = l, m
            elif nums[m] > nums[r]:
                l, r = m, r
            else:
                break

        return min(nums[l], nums[r])
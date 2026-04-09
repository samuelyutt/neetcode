class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                while r >= l and nums[r] == val:
                    r -= 1
                nums[l] = nums[r]
                r -= 1
            if r >= l:
                l += 1
        return l
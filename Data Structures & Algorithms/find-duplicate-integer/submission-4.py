class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            
            if nums[self.abs(num) - 1] < 0:
                return self.abs(num)
            nums[self.abs(num) - 1] = -nums[self.abs(num) - 1]

    def abs(self, val):
        return val if val > 0 else -val
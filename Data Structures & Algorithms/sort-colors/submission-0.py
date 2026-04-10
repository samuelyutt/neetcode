class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one = 0, 0
        for i, num in enumerate(nums):
            nums[i] = 2
            if num == 1:
                nums[one] = 1
                one += 1
            if num == 0:
                nums[one] = 1
                nums[zero] = 0
                one += 1
                zero += 1

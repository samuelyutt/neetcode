class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            tmp = nums[-1]
            for i in range(len(nums)):
                tmp, nums[i] = nums[i], tmp
        
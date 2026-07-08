class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remain = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= remain:
                remain = i

        return remain == 0
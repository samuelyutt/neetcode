class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # first house is robbed
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = nums[0] # remember this!!!!!
        for i in range(2, len(dp1)):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        # first house is not robbed
        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        for i in range(2, len(dp2)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp1[-1], dp2[-1])
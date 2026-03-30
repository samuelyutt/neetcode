class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1001] * len(nums)
        dp[0] = 0
        for i in range(len(dp)):
            j = i + 1
            while j <= i + nums[i] and j < len(nums):
                dp[j] = min(dp[j], dp[i] + 1)
                j += 1
        return dp[-1]
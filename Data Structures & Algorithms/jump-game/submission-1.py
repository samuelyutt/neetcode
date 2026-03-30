class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i, num in enumerate(nums[:-1]):
            if not dp[i]:
                continue
            j = i + 1
            while j <= i + num and j < len(nums):
                dp[j] = True
                j += 1
        return dp[-1]


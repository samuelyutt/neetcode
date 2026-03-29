class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        dp = [False] * (total // 2 + 1)
        dp[0] = True

        for num in nums:
            for i in range(len(dp) - 1, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]
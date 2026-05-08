class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 0 1 2 3 4
        # 0 0 0 0 0
        # 0 1 1 1 0
        # 0 1 2 4 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(dp)):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
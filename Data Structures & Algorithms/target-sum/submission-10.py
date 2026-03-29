class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        non_zero_nums = [abs(num) for num in nums if num != 0]
        zero_cnt = len(nums) - len(non_zero_nums)
        total = sum(non_zero_nums) + target
        if total % 2:
            return 0
        my_target = total // 2 - target

        dp = [0] * (my_target + 1)
        dp[0] = 1

        for num in non_zero_nums:
            for j in range(my_target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]

        return dp[my_target] * 2 ** zero_cnt
        
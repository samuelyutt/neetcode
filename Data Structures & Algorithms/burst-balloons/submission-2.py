class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            coins = 0
            for i in range(l, r + 1):
                coins = max(
                    coins,
                    dfs(l, i - 1) + nums[l - 1] * nums[i] * nums[r + 1] + dfs(i + 1, r)
                )
            memo[(l, r)] = coins
            return coins

        return dfs(1, len(nums) - 2)
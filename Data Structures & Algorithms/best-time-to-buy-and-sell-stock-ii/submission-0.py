class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, hold):
            if i >= len(prices):
                return 0
            if (i, hold) in memo:
                return memo[(i, hold)]
            if hold:
                ret = max(
                    prices[i] + dfs(i + 1, False), # sell
                    dfs(i + 1, True), # not sell
                )
            else:
                ret = max(
                    -prices[i] + dfs(i + 1, True), # buy
                    dfs(i + 1, False), # not buy
                )
            memo[(i, hold)] = ret
            return ret
        return dfs(0, False)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, haveCoin, cooling):
            if i >= len(prices):
                return 0
            if (i, haveCoin, cooling) in memo:
                return memo[(i, haveCoin, cooling)]

            buy, sell = 0, 0
            if haveCoin:
                sell = prices[i] + dfs(i + 1, False, True)
            else:
                if not cooling:
                    buy = -prices[i] + dfs(i + 1, True, False)

            skip = dfs(i + 1, haveCoin, False)
            ret = max(buy, sell, skip)
            memo[(i, haveCoin, cooling)] = ret
            return ret

        return max(0, dfs(0, False, False))

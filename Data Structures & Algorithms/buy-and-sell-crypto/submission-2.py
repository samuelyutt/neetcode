class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 2 3
        # 3 2 1
        # 1 3 2 4
        # 3 1 3 2 4

        min_price = 101
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            
            profit = p - min_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit
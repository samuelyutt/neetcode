class StockSpanner:

    def __init__(self):
        self.dp = [(100001, 1)] # [(price, days)]

    def next(self, price: int) -> int:
        days = 1
        while price >= self.dp[-days][0]:
            days += self.dp[-days][1]
        self.dp.append((price, days))
        return days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        for p, c in zip(profits, capital):
            h.append((c, p))
        heapq.heapify(h)
        avail_profits = []

        cnt = 0
        while cnt < k:
            while h and h[0][0] <= w:
                _, profit = heapq.heappop(h)
                heapq.heappush(avail_profits, -profit)
            if not avail_profits:
                break
            neg_profit = heapq.heappop(avail_profits)
            w -= neg_profit
            cnt += 1
        return w
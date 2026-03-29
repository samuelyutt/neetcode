class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-w for w in stones]
        heapq.heapify(h)

        while h:
            if len(h) == 1:
                return -h[0]
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)
            if (x < y):
                heapq.heappush(h, x - y)

        return 0
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = []
        for trip in trips:
            h.append((trip[1], trip[0]))
            h.append((trip[2], -trip[0]))
        heapq.heapify(h)
        
        cnt = 0
        while h:
            _, change = heapq.heappop(h)
            cnt += change
            if cnt > capacity:
                return False
        return True
class MedianFinder:

    def __init__(self):
        self.max_heap = [] # front half, -num
        self.min_heap = [] # back half, num

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        while len(self.max_heap) > len(self.min_heap):
            tmp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp)

        while len(self.min_heap) > len(self.max_heap) + 1:
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]
        
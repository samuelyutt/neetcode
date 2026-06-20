class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []

    def addNum(self, num: int) -> None:
        if len(self.a) == len(self.b):
            if len(self.b) == 0 or num < self.b[0]:
                heapq.heappush(self.a, -num)
            else:
                heapq.heappush(self.a, -heapq.heappop(self.b))
                heapq.heappush(self.b, num)
        else:
            if len(self.b) == 0 or num < self.b[0]:
                heapq.heappush(self.a, -num)
                heapq.heappush(self.b, -heapq.heappop(self.a))
            else:
                heapq.heappush(self.b, num)

    def findMedian(self) -> float:
        if len(self.a) == len(self.b):
            return (-self.a[0] + self.b[0]) / 2
        else:
            return -self.a[0]
                
        
        
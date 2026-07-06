class MedianFinder:

    def __init__(self):
        self.a = [] # min ~ mid (max heap)
        self.b = [] # mid ~ max (min heap)

    def addNum(self, num: int) -> None:
        if len(self.b) == 0 or num < self.b[0]:
            heapq.heappush(self.a, -num)
        else:
            heapq.heappush(self.b, num)

        if len(self.b) > len(self.a):
            heapq.heappush(self.a, -heapq.heappop(self.b))
        elif len(self.a) > len(self.b) + 1:
            heapq.heappush(self.b, -heapq.heappop(self.a))

    def findMedian(self) -> float:
        if len(self.a) == len(self.b):
            return (-self.a[0] + self.b[0]) / 2
        else:
            return -self.a[0]
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k or n > h[0]:
                heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
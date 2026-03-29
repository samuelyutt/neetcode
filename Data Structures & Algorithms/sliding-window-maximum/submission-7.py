class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k = 3
        # 1 2 1 1 1 3

        l, r = 0, 0
        heap = []
        res = []

        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            r += 1

            if r < k:
                continue

            while heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            l += 1

        return res

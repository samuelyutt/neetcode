class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k = 3
        # 1 2 1 1 1 3

        l, r = 0, 0
        heap = []
        window_cnts = {}
        res = []

        while r < len(nums):
            heapq.heappush(heap, -nums[r])
            window_cnts[nums[r]] = window_cnts.get(nums[r], 0) + 1
            r += 1

            if r < k:
                continue

            while True:
                num = -heap[0]
                if window_cnts.get(num, 0) == 0:
                    heapq.heappop(heap)
                else:
                    break

            res.append(num)

            window_cnts[nums[l]] -= 1
            l += 1

        return res

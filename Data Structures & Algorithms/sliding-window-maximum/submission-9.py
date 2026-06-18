class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []            
        ret = []

        for i in range(len(nums)):
            heapq.heappush(h, (-nums[i], i))

            if i < k - 1:
                continue

            while h[0][1] < i - k + 1:
                heapq.heappop(h)

            ret.append(-h[0][0])

        return ret

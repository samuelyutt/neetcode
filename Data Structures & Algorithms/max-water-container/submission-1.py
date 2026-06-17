class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        ret = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            ret = max(ret, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret
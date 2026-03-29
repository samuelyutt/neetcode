class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = -1
        l, r = 0, len(heights) - 1

        while l < r:
            hl, hr = heights[l], heights[r]
            val = min(hl, hr) * (r - l)
            if val > max_val:
                max_val = val

            if hl < hr:
                l += 1
            else:
                r -= 1

        return max_val
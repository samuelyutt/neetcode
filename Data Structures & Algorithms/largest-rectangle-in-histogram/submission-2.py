class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 7 1
        # 1 2
        # 1 3, 7 1
        # 1 4, 2 2
        # 1 5, 2 3
        # 1 6, 2 4, 4 1

        stack = [] # height, i
        ret = 0

        for i, h in enumerate(heights + [0]):
            min_i = i

            while stack and h < stack[-1][0]:
                height, hi = stack.pop()
                ret = max(ret, height * (i - hi))
                min_i = min(min_i, hi)

            if not stack or h > stack[-1][0]:
                stack.append((h, min_i))

        return ret
        
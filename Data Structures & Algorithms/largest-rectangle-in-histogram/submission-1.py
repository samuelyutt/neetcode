class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1 2
        # stack    [[1 0]] [[1 0] [2 0]] [[1 0] [2 0]]
        # max_area 0       0


        # 7 1 7 2 2 4 0

        # 7              0
        # 1              7
        # 1   7          7
        # 1   2          7
        # 1   2     4    7
        # 
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [0]):
            min_i = i
            while stack and stack[-1][0] > h:
                max_area = max(stack[-1][0] * (i - stack[-1][1]), max_area)
                _, min_i = stack.pop()
            if not stack or h > stack[-1][0]:
                stack.append([h, min_i])

        return max_area
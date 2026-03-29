class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = [0] * len(height)
        max_h = 0
        for i, h in enumerate(height):
            if h > max_h:
                max_h = h
            arr1[i] = max_h

        arr2 = [0] * len(height)
        max_h = 0
        for i, h in enumerate(reversed(height)):
            if h > max_h:
                max_h = h
            arr2[len(height) - i - 1] = max_h

        area = 0
        for i, h in enumerate(height):
            a = min(arr1[i], arr2[i]) - h
            area += a

        return area

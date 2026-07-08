class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ret = []

        for a, b in intervals:
            if not ret:
                ret.append([a, b])
            elif a <= ret[-1][1]:
                ret[-1][1] = max(b, ret[-1][1])
            else:
                ret.append([a, b])

        return ret
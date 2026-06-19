class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) and stack[-1][0] < t:
                _, j = stack.pop()
                ret[j] = i - j

            stack.append((t, i))

        return ret
            
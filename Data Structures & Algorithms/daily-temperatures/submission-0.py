class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 2 3 4 5
        # 1 3 2 4 5
        # 5 3 2 2 4
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if len(stack) == 0 or t <= stack[-1][0]:
                stack.append((t, i))
            else:
                while len(stack) != 0 and t > stack[-1][0]:
                    temp, idx = stack.pop()
                    res[idx] = i - idx
                stack.append((t, i))

        return res
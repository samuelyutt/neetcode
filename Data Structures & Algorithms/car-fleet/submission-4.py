class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append([p, (target - p) / s])
        cars.sort()

        stack = []

        for i in range(len(cars) - 1, -1, -1):
            t = cars[i][1]

            # while stack and stack[-1] >= t:
            #     stack.pop()

            # stack.append(t)

            if stack and stack[-1] >= t:
                pass
            else:
                stack.append(t)

        return len(stack)


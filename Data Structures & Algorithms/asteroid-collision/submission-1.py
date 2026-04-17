class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for cur in asteroids:
            exploded = False
            while stack and not exploded:
                prev = stack.pop()
                if prev > 0 and cur < 0:
                    if abs(prev) > abs(cur):
                        stack.append(prev)
                        exploded = True
                    elif abs(prev) < abs(cur):
                        pass
                    else:
                        exploded = True
                else:
                    stack.append(prev)
                    break
            if not exploded:
                stack.append(cur)
        return stack
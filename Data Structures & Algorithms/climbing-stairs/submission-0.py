class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 2, 1
            for i in range(n - 2):
                a, b = a + b, a
            return a
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        a, b, c = 1, 1, 0
        i = 2
        while i < n:
            a, b, c = a + b + c, a, b
            i += 1
        return a
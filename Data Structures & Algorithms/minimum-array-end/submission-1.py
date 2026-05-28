class Solution:
    def minEnd(self, n: int, x: int) -> int:
        val = 0
        m = n - 1
        mi = 0

        for xi in range(64):
            if x & 1 << xi:
                continue
            elif m & 1 << mi:
                val += 1 << xi
            mi += 1

        return x + val
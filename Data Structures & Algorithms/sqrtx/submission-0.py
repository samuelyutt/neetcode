class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1
        while l < r:
            m = (l + r + 1) // 2
            power = m**2
            if x > power:
                l = m
            elif x < power:
                r = m - 1
            else:
                return m
        return l
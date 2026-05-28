class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            lower, upper = 2**i, 2**(i + 1)
            if lower <= left < upper and lower <= right < upper:
                ret += lower
                left -= lower
                right -= lower
        return ret
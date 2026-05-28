class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            lower = 1 << i
            if lower <= left < lower << 1 and lower <= right < lower << 1:
                ret += lower
                left -= lower
                right -= lower
        return ret
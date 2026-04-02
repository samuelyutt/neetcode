class Solution:
    def getSum(self, a: int, b: int) -> int:
        t = {
            # (m, n, c): (r, c)
            (0, 0, 0): (0, 0),
            (0, 0, 1): (1, 0),
            (0, 1, 0): (1, 0),
            (1, 0, 0): (1, 0),
            (0, 1, 1): (0, 1),
            (1, 0, 1): (0, 1),
            (1, 1, 0): (0, 1),
            (1, 1, 1): (1, 1),
        }

        ret = 0
        c = 0
        for _ in range(32):
            m = a & 1
            n = b & 1
            r, c = t[(m, n, c)]
            ret = ret >> 1
            ret = ret | r * 2**31
            a = a >> 1
            b = b >> 1
        
        if ret >> 31 & 1 == 1:
            ret = ~(ret ^ 0xFFFFFFFF)
        
        return ret

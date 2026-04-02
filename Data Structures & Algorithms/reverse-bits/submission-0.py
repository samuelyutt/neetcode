class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        x = 31
        while n:
            if n % 2:
                n -= 1
                ret += 2 ** x
            n //= 2
            x -= 1
        return ret
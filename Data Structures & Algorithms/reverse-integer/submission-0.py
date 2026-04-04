class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        ret = 0
        while x:
            digit = int(math.fmod(x, 10))
            if (
                ret > MAX / 10 or
                ret < MIN / 10 or 
                (ret == MAX / 10 and digit > MAX % 10) or
                (ret == MIN / 10 and digit < MIN % 10)
            ):
                return 0
            ret *= 10
            ret += digit
            x = int(x / 10)
        return ret
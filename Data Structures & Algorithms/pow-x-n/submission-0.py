class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def f(k):
            if k == 0:
                return 1
            if k % 2:
                return x * f(k - 1)
            else:
                tmp = f(k // 2)
                return tmp * tmp

        if n >= 0:
            return f(n)
        else:
            return 1 / f(-n)
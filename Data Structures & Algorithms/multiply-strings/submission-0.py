class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #   1 2 3
        #     4 5
        # -------
        #   6 1 5
        # 4 9 2
        # -------
        # 5 5 3 5
        if num1 == '0' or num2 == '0':
            return '0'

        prods = []
        for _ in num2:
            prods.append([0] * (len(num1) + len(num2)))
        for j in range(len(num2)):
            carry = 0
            for i in range(len(num1)):
                a, b = int(num1[-i - 1]), int(num2[-j - 1])
                prod = a * b + carry
                prods[j][-j - i - 1] = prod % 10
                carry = prod // 10
            prods[j][-j - i - 2] = carry

        sums = [0] * (len(num1) + len(num2))
        carry = 0
        for i in range(len(prods[0])):
            s = carry
            for j in range(len(prods)):
                s += prods[j][-i - 1]
            sums[-i - 1] = s % 10
            carry = s // 10

        ret = ''
        for s in sums:
            if ret == '' and s == 0:
                continue
            ret += str(s)
        return ret

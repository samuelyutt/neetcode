class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = 1, 1
        carry = '0'
        ret = ''

        m = {
            '000': ('0', '0'),
            '001': ('1', '0'),
            '010': ('1', '0'),
            '100': ('1', '0'),
            '101': ('0', '1'),
            '110': ('0', '1'),
            '011': ('0', '1'),
            '111': ('1', '1'),
        }

        while i <= len(a) or j <= len(b):
            x = a[-i] if i <= len(a) else '0'
            y = b[-j] if j <= len(b) else '0'

            sum, carry = m[x + y + carry]
            ret = sum + ret

            i += 1
            j += 1

        if carry == '1':
            ret = '1' + ret

        return ret


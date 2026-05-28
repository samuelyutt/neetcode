class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        columnNumber -= 1

        while(columnNumber >= 0):
            ret = chr((columnNumber % 26) + ord('A')) + ret
            columnNumber //= 26
            columnNumber -= 1

        return ret
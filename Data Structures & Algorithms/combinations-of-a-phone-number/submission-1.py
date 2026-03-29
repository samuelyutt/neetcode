class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        cur = ''
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def search(i):
            nonlocal cur
            if i == len(digits):
                ret.append(cur)
                return
            for char in map[digits[i]]:
                cur += char
                search(i + 1)
                cur = cur[:-1]
        if len(digits) == 0:
            return []
        search(0)
        return ret
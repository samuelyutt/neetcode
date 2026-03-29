class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def search(cur, l, r):
            if r == n:
                ret.append(cur)
                return
            if l > r:
                search(cur + ')', l, r + 1)
            if n > l:
                search(cur + '(', l + 1, r)
        search('', 0, 0)
        return ret

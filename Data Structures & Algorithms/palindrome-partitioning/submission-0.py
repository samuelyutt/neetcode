class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True

        ret = []
        cur = []

        def search(i):
            if i == len(s):
                ret.append(cur.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i:j + 1]):
                    cur.append(s[i:j + 1])
                    search(j + 1)
                    cur.pop()

        search(0)
        return ret

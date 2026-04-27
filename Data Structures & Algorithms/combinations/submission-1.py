class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def search(cur, num):
            if len(cur) == k:
                nonlocal ret
                ret.append(cur.copy())
                return
            if num > n:
                return
            
            cur.append(num)
            search(cur, num + 1)
            cur.pop()
            search(cur, num + 1)

        search([], 1)
        return ret

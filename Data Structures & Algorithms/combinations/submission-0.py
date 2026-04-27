class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def search(cur, num):
            if len(cur) == k:
                nonlocal ret
                ret.append(cur)
                return
            if num > n:
                return
            
            search(cur, num + 1)
            search(cur + [num], num + 1)

        search([], 1)
        return ret

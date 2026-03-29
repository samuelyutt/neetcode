class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #    1 4 3 2, h = 9
        # 1/ 1 4 3 2 = 10
        # 2/ 1 2 2 1 = 6

        min_k, max_k = 1, max(piles)
        res = max_k
        while min_k < max_k:
            tmp_k = (min_k + max_k) // 2
            hours = self.eat(piles, tmp_k)
            if hours > h:
                min_k = tmp_k + 1
            else:
                res = min(res, tmp_k)
                max_k = tmp_k
        return res


    def eat(self, piles, k):
        hours = 0
        for p in piles:
            hours += p // k
            if p % k:
                hours += 1
        return hours
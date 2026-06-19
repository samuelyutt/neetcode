class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_within_h(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h

        l, r = 1, max(piles)
        ret = r

        while l < r:
            m = (l + r) // 2
            if not eat_within_h(m):
                l = m + 1
            else:
                r = m
        return l
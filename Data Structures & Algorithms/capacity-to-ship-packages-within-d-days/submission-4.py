class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(weight):
            day = 1
            cur = 0
            for w in weights:
                if cur + w <= weight:
                    cur += w
                else:
                    cur = w
                    day += 1
                    if day > days:
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if canShip(m):
                r = m
            else:
                l = m + 1
        return l

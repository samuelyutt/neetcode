class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def dfs(i, m, alice):
            if i >= n:
                return 0
            if (i, m, alice) in memo:
                return memo[(i, m, alice)]
            ret = 0 if alice else float('inf')
            score = 0
            for x in range(1, 2 * m + 1):
                if (i + x - 1) >= n:
                    break
                score += piles[i + x - 1]
                if alice:
                    ret = max(ret, score + dfs(i + x, max(m, x), False))
                else:
                    ret = min(ret, dfs(i + x, max(m, x), True))
            memo[(i, m, alice)] = ret
            return ret

        return dfs(0, 1, True)
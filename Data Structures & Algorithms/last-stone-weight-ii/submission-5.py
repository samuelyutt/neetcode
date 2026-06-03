class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        ret = total
        memo = {}

        def traverse(i, cur):
            nonlocal total, ret

            if i == len(stones):
                return abs(cur - (total - cur))

            if (i, cur) in memo:
                return memo[(i, cur)]

            memo[(i, cur)] = min(
                traverse(i + 1, cur),
                traverse(i + 1, cur + stones[i])
            )
            return memo[(i, cur)]

        return traverse(0, 0)
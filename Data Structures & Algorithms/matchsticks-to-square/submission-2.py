class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        
        n = len(matchsticks)
        side = sum(matchsticks) // 4
        used = [False] * n
        used_cnt = 0

        def search(i, cur, cnt):
            nonlocal n, side, used, used_cnt
            if cnt == 4 and used_cnt == n:
                return True

            ret = False
            prev = None
            for idx in range(i, n):
                if used[idx]:
                    continue
                if matchsticks[idx] == prev:
                    continue
                prev = matchsticks[idx]
                used[idx] = True
                used_cnt += 1
                if cur + matchsticks[idx] < side:
                    ret |= search(idx + 1, cur + matchsticks[idx], cnt)
                elif cur + matchsticks[idx] == side:
                    ret |= search(0, 0, cnt + 1)
                used[idx] = False
                used_cnt -= 1
            return ret
        
        return search(0, 0, 0)
                
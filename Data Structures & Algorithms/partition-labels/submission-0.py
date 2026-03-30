class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        memo = {}
        for c in s:
            memo[c] = 1 + memo.get(c, 0)
        ret, cnt, cur = [], 0, set()
        for c in s:
            cnt += 1
            cur.add(c)
            memo[c] -= 1
            if memo[c] == 0:
                cur.remove(c)
            if len(cur) == 0:
                ret.append(cnt)
                cnt = 0
        return ret
            
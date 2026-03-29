class Solution:
    def numDecodings(self, s: str) -> int:
        ret = 0
        q = deque([(0, 0)]) # [(l, r)]
        while q:
            l, r = q.popleft()
            if s[l] == '0':
                continue
            if not 1 <= int(s[l:r + 1]) <= 26:
                continue
            if r == len(s) - 1:
                # last digit
                ret += 1
            elif l == r:
                # 1 digit
                q.append((l, r + 1))
                q.append((l + 1, r + 1))
            else:
                # 2 digits
                q.append((r + 1, r + 1))
        return ret
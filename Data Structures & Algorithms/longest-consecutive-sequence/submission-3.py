class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0

        while s:
            q = deque([s.pop()])
            cnt = 0

            while q:
                num = q.popleft()
                cnt += 1

                if (num + 1) in s:
                    q.append(num + 1)
                    s.remove(num + 1)

                if (num - 1) in s:
                    q.append(num - 1)
                    s.remove(num - 1)

            ret = max(ret, cnt)

        return ret

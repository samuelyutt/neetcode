class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0

        while nums:
            q = deque([nums.pop()])
            cnt = 0
            while q:
                cnt += 1
                num = q.pop()
                if (num + 1) in nums:
                    q.append(num + 1)
                    nums.remove(num + 1)
                if (num - 1) in nums:
                    q.append(num - 1)
                    nums.remove(num - 1)
            ret = max(ret, cnt)

        return ret


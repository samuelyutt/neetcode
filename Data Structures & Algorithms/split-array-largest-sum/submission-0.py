class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(sum):
            cnt = 1
            cur_sum = 0
            for num in nums:
                if cur_sum + num <= sum:
                    cur_sum += num
                else:
                    cnt += 1
                    cur_sum = num
            return cnt <= k

        l, r = max(nums), sum(nums)
        while l < r:
            m = (l + r) // 2
            if canSplit(m):
                r = m
            else:
                l = m + 1
        return r
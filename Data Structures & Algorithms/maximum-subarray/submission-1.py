class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        cur = 0

        for num in nums:
            cur += num
            ret = max(ret, cur)
            cur = max(0, cur)

        return ret
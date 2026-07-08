class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = max(nums)

        tmp = 0
        for num in nums:
            tmp += num
            ret = max(ret, tmp)
            tmp = max(tmp, 0)

        return ret
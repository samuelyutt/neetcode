class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        tmp = 0

        for num in nums:
            ret = max(ret, tmp + num)
            if tmp + num < 0:
                tmp = 0
            else:
                tmp += num

        return ret
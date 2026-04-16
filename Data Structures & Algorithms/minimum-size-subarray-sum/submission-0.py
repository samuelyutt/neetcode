class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = cur_sum = 0
        ret = 100001
        while r < len(nums):
            cur_sum += nums[r]
            while l <= r and cur_sum >= target:
                ret = min(ret, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            r += 1
        return ret if ret != 100001 else 0
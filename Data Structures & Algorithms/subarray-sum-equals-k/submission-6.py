class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        n = len(nums)
        acc_sum_cnts = {}
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            # cur_sum = k
            if cur_sum == k:
                ret += 1
            # cur_sum - diff = k
            diff = cur_sum - k
            ret += acc_sum_cnts.get(diff, 0)
            acc_sum_cnts[cur_sum] = acc_sum_cnts.get(cur_sum, 0) + 1
        return ret
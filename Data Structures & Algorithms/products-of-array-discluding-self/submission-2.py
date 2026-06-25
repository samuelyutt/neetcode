class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l = [0] * n
        l[0] = nums[0]
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i]

        r = [0] * n
        r[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i]

        ret = [1] * n

        for i in range(n):
            if i > 0:
                ret[i] *= l[i - 1]
            if i < n - 1:
                ret[i] *= r[i + 1]

        return ret
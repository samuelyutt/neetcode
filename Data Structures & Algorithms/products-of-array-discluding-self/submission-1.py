class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 2:
            return [nums[1], nums[0]]

        pre = [0] * n
        suf = [0] * n
        
        pre[0] = nums[0]
        suf[-1] = nums[-1]

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]

        ret = []
        ret.append(suf[1])
        for i in range(1, n - 1):
            ret.append(pre[i - 1] * suf[i + 1])
        ret.append(pre[n - 2])

        return ret

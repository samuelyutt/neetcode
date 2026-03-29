class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = nums[0]
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            ret = max(ret, prod)
            if nums[i] == 0:
                prod = 1
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            ret = max(ret, prod)
            if nums[i] == 0:
                prod = 1
        return ret
            
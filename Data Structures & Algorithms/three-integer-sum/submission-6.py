class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = set()

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                val = nums[i] + nums[l] + nums[r]
                
                if val == 0:
                    ret.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1

        return list(ret)
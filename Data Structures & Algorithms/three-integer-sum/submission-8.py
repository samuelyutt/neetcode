class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = []

        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return ret
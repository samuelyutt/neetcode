class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -1 0 1
        # 0 0 0
        # -1 0 0 0 0 0 1

        # Sort
        # For each value
        #   if larger than 0: break
        #   if the same as previous: continue
        #   two pointer two sum
        #   if sum != target:
        #       move pointers
        #   else:
        #       move pointers until different
        res = []

        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = v + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
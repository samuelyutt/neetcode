class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()
        def search(cur_subset, idx):
            if idx >= len(nums):
                return
            num = nums[idx]
            ret.append(cur_subset + [num])
            search(cur_subset + [num], idx + 1)
            while idx < len(nums) and nums[idx] == num:
                idx += 1
            search(cur_subset, idx)
        search([], 0)
        return ret
        
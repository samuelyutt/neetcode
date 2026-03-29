class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def search(cur_subset, used):
            nonlocal ret
            if len(cur_subset) == len(nums):
                ret.append(cur_subset)
                return
            for i, u in enumerate(used):
                if not u:
                    used[i] = True
                    search(cur_subset + [nums[i]], used)
                    used[i] = False
        search([], [False] * len(nums))
        return ret

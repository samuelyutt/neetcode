class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def search(cur_subset, used):
            nonlocal ret
            if len(cur_subset) == len(nums):
                ret.append(cur_subset.copy())
                return
            for i, u in enumerate(used):
                if not u:
                    used[i] = True
                    cur_subset.append(nums[i])
                    search(cur_subset, used)
                    used[i] = False
                    cur_subset.pop()
        search([], [False] * len(nums))
        return ret

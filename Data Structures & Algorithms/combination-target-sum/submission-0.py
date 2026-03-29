class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def search(target, cur_subset):
            nonlocal ret
            for n in nums:
                if cur_subset and n < cur_subset[-1]:
                    continue
                if n < target:
                    search(target - n, cur_subset + [n])
                elif n == target:
                    ret.append(cur_subset + [n])
        ret = []
        search(target, [])
        return ret

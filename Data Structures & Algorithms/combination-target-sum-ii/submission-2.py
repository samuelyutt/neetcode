class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
    
        def search(idx, cur_subset, cur_sum):
            if idx >= len(candidates):
                return
            num = candidates[idx]
            s = cur_sum + num
            if s == target:
                ret.append(cur_subset + [num])
            elif s < target:
                search(idx + 1, cur_subset + [num], s)
                while idx < len(candidates) and candidates[idx] == num:
                    idx += 1
                search(idx, cur_subset, cur_sum)
        search(0, [], 0)
        return ret

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
    
        def search(idx, cur_subset):
            if idx >= len(candidates):
                return
            num = candidates[idx]
            s = sum(cur_subset)
            if s + num == target:
                ret.append(cur_subset + [num])
            elif s + num < target:
                search(idx + 1, cur_subset + [num])
                while idx < len(candidates) and candidates[idx] == num:
                    idx += 1
                search(idx, cur_subset)
        search(0, [])
        return ret

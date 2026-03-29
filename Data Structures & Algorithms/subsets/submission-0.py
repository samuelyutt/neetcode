class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2**len(nums)):
            subset = []
            for j, val in enumerate(nums):
                if (i // 2**j) % 2:
                    subset.append(val)
            ret.append(subset)
        return ret
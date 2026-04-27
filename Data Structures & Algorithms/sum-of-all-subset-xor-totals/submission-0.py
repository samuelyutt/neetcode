class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        results = [0]
        for num in nums:
            new = []
            for r in results:
                new.append(r ^ num)
            results += new
        return sum(results)
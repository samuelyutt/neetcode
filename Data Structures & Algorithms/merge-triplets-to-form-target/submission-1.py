class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        memo = [0] * 3
        for triplet in triplets:
            ignore = False
            for i in range(3):
                if triplet[i] > target[i]:
                    ignore = True
                    break
            if ignore:
                continue
            for i in range(3):
                memo[i] = max(memo[i], triplet[i])
        return memo == target
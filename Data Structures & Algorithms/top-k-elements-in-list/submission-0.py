class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        res = sorted([(d[num], num) for num in d])[-k:]
        return [num for (_, num) in res]

            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        arr = [(val, key) for key, val in d.items()]
        arr.sort()

        ret = []
        for i in range(k):
            ret.append(arr[-i - 1][1])

        return ret
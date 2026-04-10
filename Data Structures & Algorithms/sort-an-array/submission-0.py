class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        arr = [0] * (max_val - min_val + 1)
        for num in nums:
            arr[num - min_val] += 1
        ret = []
        for i, cnt in enumerate(arr):
            ret += [i + min_val] * cnt
        return ret
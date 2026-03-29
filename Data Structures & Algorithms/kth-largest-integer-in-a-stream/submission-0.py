class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        i = 0
        for v in self.nums:
            if val < v:
                break
            i += 1
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        print(val, self.nums)
        return self.nums[-self.k]


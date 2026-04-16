class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        s = set()
        while r <= k and r < len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            r += 1

        s.remove(nums[l])
        l += 1

        while r < len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            s.remove(nums[l])
            l += 1
            r += 1

        return False

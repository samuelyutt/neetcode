class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = None
        cnt = 0
        for num in nums:
            if ret is None or cnt == 0:
                ret = num
            if ret == num:
                cnt += 1
            else:
                cnt -= 1
        return ret
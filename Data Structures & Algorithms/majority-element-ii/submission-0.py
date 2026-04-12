class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if len(count) > 2:
                for num in count:
                    count[num] -= 1
                tmp = []
                for num in count:
                    if count[num] == 0:
                        tmp.append(num)
                for num in tmp:
                    del count[num]
        ret = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                ret.append(num)
        return ret
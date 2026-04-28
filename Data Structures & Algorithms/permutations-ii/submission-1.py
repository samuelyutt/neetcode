class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set([(nums[0],)])

        for num in nums[1:]:
            new = set()
            while ret:
                permutation = list(ret.pop())
                new.add(tuple([num] + permutation))
                for i in range(len(permutation)):
                    if num == permutation[i]:
                        continue
                    new.add(tuple(permutation[:i + 1] + [num] + permutation[i + 1:]))
            ret = new

        return list(ret)

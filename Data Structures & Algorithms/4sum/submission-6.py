class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        searched = set()

        def search(a, d):
            if (a, d) in searched:
                return
            searched.add((a, d))
            if a >= d:
                return
            if nums[a] > target:
                return
            b, c = a + 1, d - 1
            while b < c:
                if nums[a] + nums[b] > target:
                    break
                sum4 = nums[a] + nums[b] + nums[c] + nums[d]
                if sum4 > target:
                    c -= 1
                elif sum4 < target:
                    b += 1
                else:
                    res.add((nums[a], nums[b], nums[c], nums[d]))
                    b += 1
                    c -= 1
            search(a, d - 1)
            search(a + 1, d)

        search(0, len(nums) - 1)

        ret = []
        for quad in res:
            ret.append(list(quad))
        return ret

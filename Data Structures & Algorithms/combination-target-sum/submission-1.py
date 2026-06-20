class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        cur = []
        cur_sum = 0

        def search(i):
            nonlocal cur_sum

            if i == len(nums):
                if cur_sum == target:
                    ret.append(cur.copy())
                return

            if cur_sum > target:
                return

            cur.append(nums[i])
            cur_sum += nums[i]
            search(i)

            cur.pop()
            cur_sum -= nums[i]
            search(i + 1)

        search(0)

        return ret

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = []

        cur = []
        cur_sum = 0

        def dfs(i):
            nonlocal cur_sum
            
            if i == len(nums):
                return
            if cur_sum > target:
                return

            cur_sum += nums[i]
            cur.append(nums[i])

            if cur_sum == target:
                ret.append(cur.copy())
            elif cur_sum < target:
                dfs(i)

            cur_sum -= nums[i]
            cur.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j)

        dfs(0)

        return ret


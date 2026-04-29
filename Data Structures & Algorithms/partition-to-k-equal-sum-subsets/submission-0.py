class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        target = sum(nums) // k
        nums.sort()
        n = len(nums)
        used = [False] * n
        used_cnt = 0

        def search(i, cur_sum, cnt):
            nonlocal used_cnt, n
            if cnt == k and used_cnt == n:
                return True

            ret = False
            prev = None
            for idx in range(i, n):
                if used[idx]:
                    continue
                if prev == nums[idx]:
                    continue

                prev = nums[idx]
                used[idx] = True
                used_cnt += 1
                if cur_sum + nums[idx] < target:
                    ret |= search(idx + 1, cur_sum + nums[idx], cnt)
                elif cur_sum + nums[idx] == target:
                    ret |= search(0, 0, cnt + 1)
                used[idx] = False
                used_cnt -= 1

                if ret:
                    return True
                if cur_sum + nums[idx] > target:
                    break
                
            return ret
        
        return search(0, 0, 0)
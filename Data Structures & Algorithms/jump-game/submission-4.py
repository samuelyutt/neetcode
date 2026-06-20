class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visit = [False] * len(nums)
        visit[0] = True

        for i in range(len(nums)):
            if visit[i]:
                for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                    visit[j] = True
        
        return visit[-1]
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        arr = nums.copy()
        for num in nums[:n - 1]:
            arr.append(num)
        n_arr = len(arr)

        ret = float('-inf')
        dp = []
        for _ in range(n_arr):
            dp.append([0] * (n_arr))
        for l in range(n_arr - 1, -1, -1):
            for r in range(l, n_arr):
                if l == r:
                    dp[l][r] = arr[l]
                elif r - l == 1:
                    dp[l][r] = arr[l] + arr[r]
                elif r - l < n:
                    dp[l][r] = max(
                        arr[l] + dp[l + 1][r],
                        arr[r] + dp[l][r - 1],
                    )
                else:
                    break
                ret = max(ret, dp[l][r])

        return ret
        
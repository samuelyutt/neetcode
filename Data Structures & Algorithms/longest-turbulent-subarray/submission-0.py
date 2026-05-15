class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        # [2,4,3,2,2,5,1,4]
        # 2 -1 -1 0 3 -4 3
        diff = []
        for i in range(1, len(arr)):
            diff.append(arr[i] - arr[i - 1])
        
        ret, cur = 1, 0
        l = r = 0
        while l <= r < len(diff):
            if l == r:
                if diff[l] == 0:
                    cur = 0
                    l = r = r + 1
                else:
                    cur = 1
                    r += 1
            elif diff[r] * diff[r - 1] < 0:
                r += 1
                cur = r - l
            else:
                cur = 0
                l = r
            ret = max(ret, cur + 1)
        return ret
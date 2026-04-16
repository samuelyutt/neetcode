class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a, b = 0, len(arr) - 1
        while a != b:
            m = (a + b + 1) // 2
            print(a, b, m, arr[m] <= x)
            if x >= arr[m]:
                a = m
            else:
                b = m - 1

        if a < len(arr) - 1 and x - arr[a] > arr[a + 1] - x:
            a += 1

        l, r = a, a
        while r - l + 1 < k:
            if r == len(arr) - 1:
                l -= 1
            elif l == 0:
                r += 1
            else:
                if x - arr[l - 1] <= arr[r + 1] - x:
                    l -= 1
                    r -= 1
                else:
                    r += 1
        return arr[l:r + 1]



class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max idx
        def findMax():
            l, r = 0, mountainArr.length() - 1
            while l < r:
                if r - l == 1:
                    if mountainArr.get(l) < mountainArr.get(r):
                        return r
                    else:
                        return l
                else:
                    m = (l + r + 1) // 2
                    a, b = mountainArr.get(m - 1), mountainArr.get(m + 1)
                    if a < b:
                        l = m
                    elif a > b:
                        r = m
                    else:
                        l += 1
            return r

        max_i = findMax()
        
        # find in left part
        l, r = 0, max_i
        if mountainArr.get(l) <= target <= mountainArr.get(r):
            while l <= r:
                m = (l + r + 1) // 2
                val = mountainArr.get(m)
                if target == val:
                    return m
                elif target > val:
                    l = m + 1
                else:
                    r = m - 1

        # find in right part
        l, r = max_i + 1, mountainArr.length() - 1
        if mountainArr.get(l) >= target >= mountainArr.get(r):
            while l <= r:
                m = (l + r + 1) // 2
                val = mountainArr.get(m)
                if target == val:
                    return m
                elif target > val:
                    r = m - 1
                else:
                    l = m + 1

        return -1
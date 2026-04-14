class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i, j, k = 0, 0, 0
        while i < m + n:
            cmp = []
            if i < m:
                cmp.append(nums1[i])
            if j < n:
                cmp.append(nums2[j])
            if k < len(nums3):
                cmp.append(nums3[k])
            num = min(cmp)

            if i < m and num == nums1[i]:
                i += 1
            elif j < n and num == nums2[j]:
                if i < m:
                    nums3.append(nums1[i])
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif k < len(nums3) and num == nums3[k]:
                if i < m:
                    nums3.append(nums1[i])
                nums1[i] = nums3[k]
                i += 1
                k += 1
        
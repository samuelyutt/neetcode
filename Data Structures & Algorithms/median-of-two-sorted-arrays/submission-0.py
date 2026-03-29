class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKth(A, B, k):
            if len(A) > len(B):
                A, B = B, A # A is always smaller
            if len(A) == 0:
                return B[k]
            if k == 0:
                return min(A[0], B[0])

            i = min(len(A) - 1, (k - 1) // 2)
            j = min(len(B) - 1, (k - 1) // 2)

            if A[i] < B[j]:
                return getKth(A[i + 1:], B, k - i - 1)
            else:
                return getKth(A, B[j + 1:], k - j - 1)

        cnt = (len(nums1) + len(nums2))
        if (cnt % 2):
            return getKth(nums1, nums2, cnt // 2)
        else:
            return (getKth(nums1, nums2, cnt // 2 - 1) + getKth(nums1, nums2, cnt // 2)) / 2

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [1, 2, 3]
        # [1, 2, 10, 11]
        # [1, 1, 2, 3]

        d = set()
        for n in nums:
            d.add(n)

        max_cnt = 0       
        for n in nums:
            if not (n - 1) in d:
                cnt = 1
                while n + cnt in d:
                    cnt += 1
                max_cnt = max(cnt, max_cnt)

        return max_cnt
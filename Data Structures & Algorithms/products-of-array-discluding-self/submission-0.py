class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3]
        # [6, 3, 2]

        # [0, 1, 2]
        # [2, 0, 0]

        # [0, 0, 2]
        # [0, 0, 0]

        nZero = 0
        allProd = 1
        for num in nums:
            if num:
                allProd *= num
            else:
                nZero += 1
        
        res = []
        for num in nums:
            if nZero > 1:
                res.append(0)
            elif nZero == 1:
                if num:
                    res.append(0)
                else:
                    res.append(allProd)
            else:
                res.append(allProd // num)

        return res

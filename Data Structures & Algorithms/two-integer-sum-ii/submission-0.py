class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while numbers[index1] + numbers[index2] != target:
            val = target - numbers[index1]
            while val < numbers[index2]:
                index2 -= 1
            if val > numbers[index2]:
                index1 += 1

        return [index1 + 1, index2 + 1]
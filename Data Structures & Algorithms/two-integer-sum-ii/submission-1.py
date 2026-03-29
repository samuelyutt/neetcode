class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        sum = numbers[index1] + numbers[index2]

        while sum != target:
            if sum > target:
                index2 -= 1
            else:
                index1 += 1
            sum = numbers[index1] + numbers[index2]

        return [index1 + 1, index2 + 1]
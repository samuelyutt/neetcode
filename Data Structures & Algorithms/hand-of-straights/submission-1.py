class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        arr = [0] * (max(hand) + 1)
        for num in hand:
            arr[num] += 1
        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            elif arr[i] > 0:
                cnt = arr[i]
                for j in range(groupSize):
                    if i + j >= len(arr):
                        return False
                    arr[i + j] -= cnt
            elif arr[i] < 0:
                return False
        return True
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target 10
        # position 1 4
        # speed    3 2
        # 
        # idx 0 1 2 3 4 5 6 7 8 9
        # arr 0 3 0 0 3 0 0 0 0 0
        # fleets [3] -> [3]

        # target 10
        # position 4 1 7 0
        # speed    2 2 1 1
        # 
        # idx 0 1   2 3 4 5 6 7 8 9
        # arr 5 4.5 0 0 3 0 0 3 0 0
        # fleets [5] -> [5, 4.5] -> [5, 4.5, 3]

        # target 10
        # position 0 4 2
        # speed    2 1 3
        # 
        # idx 0 1 2  3 4 5 6 7 8 9
        # arr 5 0 2+ 0 6 0 0 0 0 0
        # fleets [5] -> [5, 2] -> [5, 6]

        # slow car at front

        arr = [0] * target # hours to target at each mile
        for p, s in zip(position, speed):
            arr[p] = (target - p) / s

        fleets = []    
        for i in range(target):
            if arr[i] == 0:
                continue
            while fleets and fleets[-1] <= arr[i]:
                fleets.pop()
            fleets.append(arr[i])

        return len(fleets)
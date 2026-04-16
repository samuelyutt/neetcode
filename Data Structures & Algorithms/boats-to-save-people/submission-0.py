class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people.reverse()
        ret = 0
        boats = []
        cnt = 0
        for weight in people:
            if boats and boats[-1] + weight <= limit:
                boats.pop()
                cnt += 1
            else:
                boats.append(weight)
        return cnt + len(boats)
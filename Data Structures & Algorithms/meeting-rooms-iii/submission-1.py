class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heapq.heapify(meetings) # [[start, end]]

        rooms = [[0, i] for i in range(n)]
        heapq.heapify(rooms) # [[until, room_i]]

        avail_rooms = []
        
        cnt = [0] * n

        while meetings:
            s, e = heapq.heappop(meetings)
            duration = e - s

            while rooms and rooms[0][0] <= s:
                until, i = heapq.heappop(rooms)
                heapq.heappush(avail_rooms, [i, until])
            
            if avail_rooms:
                i, until = heapq.heappop(avail_rooms)
            else:
                until, i = heapq.heappop(rooms)

            s = max(until, s)

            heapq.heappush(rooms, [s + duration, i])
            cnt[i] += 1

        max_cnt = max(cnt)
        return cnt.index(max_cnt)
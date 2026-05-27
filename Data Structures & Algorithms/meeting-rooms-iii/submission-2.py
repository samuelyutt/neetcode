class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heapq.heapify(meetings) # [[start, end]]

        rooms = [[0, i] for i in range(n)] # [[until, room_i]]
        heapq.heapify(rooms)

        avail_rooms = []  # [[room_i, until]]

        cnt = [0] * n

        while meetings:
            # pop the next meeting
            s, e = heapq.heappop(meetings)
            duration = e - s

            # check avail rooms
            while rooms and rooms[0][0] <= s:
                until, i = heapq.heappop(rooms)
                heapq.heappush(avail_rooms, [i, until])
            
            if avail_rooms:
                # use the first avail room
                i, until = heapq.heappop(avail_rooms)
            else:
                # wait for the first occupied room to be avail
                until, i = heapq.heappop(rooms)

            s = max(until, s)

            heapq.heappush(rooms, [s + duration, i])
            cnt[i] += 1

        max_cnt = max(cnt)
        return cnt.index(max_cnt)
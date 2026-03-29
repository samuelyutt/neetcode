class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {} # task -> count
        for t in tasks:
            d[t] = d.get(t, 0) + 1

        max_heap = [(-c, t) for t, c in d.items()] # (-count, task)
        heapq.heapify(max_heap)

        q = [None] * n # (-count, task)
        q = deque(q)

        ret = 0
        while d:
            ret += 1
            if max_heap:
                c, t = heapq.heappop(max_heap)
                c += 1
                if c != 0:
                    q.append((c, t))
                    d[t] = -c
                else:
                    q.append(None)
                    del d[t]
            else:
                q.append(None)

            tmp = q.popleft()
            if tmp is not None:
                heapq.heappush(max_heap, tmp)

        return ret

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # u -> [(v, t)]
        for t in times:
            u, v, t = tuple(t)
            adj[u].append((v, t))

        recv_time = [-1] * n
        q = deque([(k, 0)])
        while q:
            u, cur_time = q.popleft()
            if recv_time[u - 1] == -1 or cur_time < recv_time[u - 1]:
                recv_time[u - 1] = cur_time
                for v, t in adj[u]:
                    q.append((v, cur_time + t))
        
        ret = 0
        for t in recv_time:
            if t == -1:
                return -1
            ret = max(ret, t)
        return ret

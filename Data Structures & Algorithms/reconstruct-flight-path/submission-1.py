class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for ticket in tickets:
            d[ticket[0]].append([ticket[1], False])
        for key in d:
            d[key].sort()

        path = ['JFK']
        ret = None
        def dfs(ticket):
            nonlocal ret
            if ret:
                return
            cur, used = ticket
            if used:
                return
            path.append(cur)
            if ret is None and len(path) >= len(tickets) + 1:
                ret = path.copy()
                return
            ticket[1] = True
            for next_ticket in d[cur]:
                dfs(next_ticket)
            path.pop()
            ticket[1] = False

        for ticket in d['JFK']:
            dfs(ticket)

        return ret

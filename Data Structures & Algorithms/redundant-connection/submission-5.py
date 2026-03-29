class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        root = edges[0][0]
        traversed = set([root])
        adj = {i + 1: set() for i in range(n)}
        q = deque()

        for e in edges:

            if e[0] in traversed and e[1] in traversed:
                return e
            elif e[0] in traversed:
                adj[e[0]].add(e[1])
                q.append(e[1])
            elif e[1] in traversed:
                adj[e[1]].add(e[0])
                q.append(e[0])
            else:
                adj[e[0]].add(e[1])
                adj[e[1]].add(e[0])

            while q:
                node = q.popleft()
                if node in traversed:
                    return e
                traversed.add(node)
                for neighbor in adj[node]:
                    adj[neighbor].remove(node)
                    q.append(neighbor)

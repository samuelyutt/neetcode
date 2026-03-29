class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = {i + 1: set() for i in range(n)}
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])

            traversed = set()
            root = edges[0][0]
            q = deque([(root, None)])
            while q:
                node, prev = q.popleft()
                if node in traversed:
                    return e
                traversed.add(node)
                for neighbor in adj[node]:
                    if neighbor != prev:
                        q.append((neighbor, node))

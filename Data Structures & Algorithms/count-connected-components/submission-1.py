class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}
        for edge in edges:
            if edge[0] == edge[1]:
                continue
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        ret = 0
        not_traversed = set([i for i in range(n)])
        while not_traversed:
            ret += 1
            root = not_traversed.pop()
            not_traversed.add(root)
            q = deque([root])
            while q:
                node = q.pop()
                if node not in not_traversed:
                    continue
                not_traversed.remove(node)
                for neighbor in adj[node]:
                    q.append(neighbor)
        return ret
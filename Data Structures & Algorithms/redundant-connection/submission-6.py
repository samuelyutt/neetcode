class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        d = {i: i for i in range(1, n + 1)} # node -> group
        g = {i: set([i]) for i in range(1, n + 1)} # group -> nodes

        for a, b in edges:
            group_a = d[a]
            group_b = d[b]

            if group_a == group_b:
                return [a, b]

            for node in g[group_b]:
                g[group_a].add(node)
                d[node] = group_a

            del g[group_b]

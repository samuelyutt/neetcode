class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]


class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 1 for i in range(1, n + 1)}

    def find(self, node):
        cur = node
        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]

        return True
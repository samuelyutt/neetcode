class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False

        return n == dsu.rank[dsu.find(0)]


class DSU:

    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu

        self.rank[pu] += self.rank[pv]
        self.parent[pv] = self.parent[pu]

        return True
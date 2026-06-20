class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        root = dsu.find(0)
        return dsu.ranks[root] == n


class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.ranks = {i: 1 for i in range(n)}

    def find(self, node):
        cur = node
        while cur != self.parents[cur]:
            self.parents[cur] = self.parents[self.parents[cur]]
            cur = self.parents[cur]
        return cur
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.ranks[pv] > self.ranks[pu]:
            pu, pv = pv, pu

        self.parents[pv] = pu
        self.ranks[pu] += self.ranks[pv]

        return True
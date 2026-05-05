class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i) # [v1, v2, weight, i]
        edges.sort(key=lambda edge: edge[2])
        
        # Find MST weight
        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critcal, pseudo = [], []
        for cur_v1, cur_v2, cur_w, cur_i in edges:
            # use this edge
            w1 = cur_w
            uf1 = UnionFind(n)
            uf1.union(cur_v1, cur_v2)
            for v1, v2, w, i in edges:
                if i != cur_i and uf1.union(v1, v2):
                    w1 += w
            
            # withdraw this edge
            w2 = 0
            uf2 = UnionFind(n)
            for v1, v2, w, i in edges:
                if i != cur_i and uf2.union(v1, v2):
                    w2 += w

            if w1 == w2 == mst_weight and max(uf1.rank) == max(uf2.rank) == max(uf.rank):
                pseudo.append(cur_i)
            elif w1 == mst_weight and max(uf1.rank) == max(uf.rank):
                critcal.append(cur_i)
        
        return [critcal, pseudo]


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v):
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]] # why? -> path compression
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            # merge p2 -> p1
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            # merge p1 -> p2
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

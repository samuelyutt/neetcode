class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        names = {}

        for values in accounts:
            name = values[0]

            for mail in values[1:]:
                dsu.parent[mail] = mail
                dsu.rank[mail] = 1
                names[mail] = name

        for values in accounts:
            for i in range(2, len(values)):
                dsu.union(values[i - 1], values[i])

        d = {}
        for mail in dsu.parent:
            p = dsu.find(mail)

            if p not in d:
                d[p] = []

            d[p].append(mail)

        ret = []
        for values in d.values():
            name = names[values[0]]
            values.sort()
            ret.append([name] + values)
        return ret


class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        
        self.parent[pv] = self.parent[pu]
        self.rank[pu] += self.rank[pv]
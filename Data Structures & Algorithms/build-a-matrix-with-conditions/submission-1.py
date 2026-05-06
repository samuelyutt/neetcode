class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        coords = {}

        # rows
        indegree = [0] * (k + 1)
        conds = defaultdict(list)
        for a, b in rowConditions:
            indegree[b] += 1
            conds[a].append(b)
        q = deque([i for i in range(k + 1) if i > 0 and indegree[i] == 0])
        r = 0
        while q:
            val = q.popleft()
            coords[val] = [r]
            r += 1
            for b in conds[val]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    q.append(b)
        if r != k:
            return []

        # cols
        indegree = [0] * (k + 1)
        conds = defaultdict(list)
        for a, b in colConditions:
            indegree[b] += 1
            conds[a].append(b)
        q = deque([i for i in range(k + 1) if i > 0 and indegree[i] == 0])
        c = 0
        while q:
            val = q.popleft()
            coords[val].append(c)
            c += 1
            for b in conds[val]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    q.append(b)
        if c != k:
            return []

        ret = []
        for _ in range(k):
            ret.append([0] * k)
        for val, (x, y) in coords.items():
            ret[x][y] = val
        return ret
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        coords = {}

        # rows
        pre_cnts = [0] * (k + 1)
        conds = defaultdict(list)
        for a, b in rowConditions:
            pre_cnts[b] += 1
            conds[a].append(b)
        avail_q_row = deque([i for i in range(k + 1) if i > 0 and pre_cnts[i] == 0])
        r = 0
        while avail_q_row:
            val = avail_q_row.popleft()
            coords[val] = [r]
            r += 1
            for b in conds[val]:
                pre_cnts[b] -= 1
                if pre_cnts[b] == 0:
                    avail_q_row.append(b)
        if r != k:
            return []

        # cols
        pre_cnts = [0] * (k + 1)
        conds = defaultdict(list)
        for a, b in colConditions:
            pre_cnts[b] += 1
            conds[a].append(b)
        avail_q_col = deque([i for i in range(k + 1) if i > 0 and pre_cnts[i] == 0])
        c = 0
        while avail_q_col:
            val = avail_q_col.popleft()
            coords[val].append(c)
            c += 1
            for b in conds[val]:
                pre_cnts[b] -= 1
                if pre_cnts[b] == 0:
                    avail_q_col.append(b)
        if c != k:
            return []

        ret = []
        for _ in range(k):
            ret.append([0] * k)
        for val, coord in coords.items():
            ret[coord[0]][coord[1]] = val
        return ret
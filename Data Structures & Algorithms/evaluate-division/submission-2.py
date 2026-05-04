class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        groups = {} # group_id -> set(name)
        records = {} # name -> [group_id, factor]

        group_id = 0
        for eq, val in zip(equations, values):
            a, b = eq
            if a in records and b in records and records[a][0] != records[b][0]:
                # merge two groups: a -> b
                a_group, b_group = records[a][0], records[b][0]
                for name in groups[a_group]:
                    records[name][0] = b_group
                    records[name][1] *= val
                groups[b_group].update(groups[a_group])
                del groups[a_group]

            if a not in records and b not in records:
                # new group: add a, b to new group
                groups[group_id] = set([a, b])
                records[a] = [group_id, val]
                records[b] = [group_id, 1]
                group_id += 1
            else:
                # add a and b to an existed group

                # b is always in record
                if b not in records:
                    a, b = b, a
                    val = 1 / val

                # add a to record
                b_group = records[b][0]
                groups[b_group].add(a)
                records[a] = [b_group, val * records[b][1]]

        ret = []
        for x, y in queries:
            if x in records and y in records and records[x][0] == records[y][0]:
                ret.append(records[x][1] / records[y][1])
            else:
                ret.append(-1)
        return ret
                
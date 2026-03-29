class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i: set() for i in range(n)} # node -> set(neighbors)
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if n1 == n2:
                return False
            d[n1].add(n2)
            d[n2].add(n1)

        traversed = set()
        q = deque([0])
        while q:
            node = q.popleft()
            if node in traversed:
                return False
            traversed.add(node)
            for neighbor in d[node]:
                d[neighbor].discard(node)
                q.append(neighbor)

        if len(traversed) == n:
            return True
        else:
            return False
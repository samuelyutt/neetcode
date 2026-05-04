class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = {i: Node(i) for i in range(n)} # key -> node
        for i, j in edges:
            nodes[i].neighbors.add(j)
            nodes[i].degree += 1
            nodes[j].neighbors.add(i)
            nodes[j].degree += 1

        ret = []
        candidates = set([i for i in range(n) if len(nodes[i].neighbors) <= 1])
        while candidates:
            ret = list(candidates)
            new_candidates = set()
            for i in candidates:
                node = nodes[i]
                if not node.neighbors:
                    continue
                j = node.neighbors.pop()
                next = nodes[j]
                next.neighbors.remove(i)
                if len(next.neighbors) == 1:
                    new_candidates.add(j)
            candidates = new_candidates
        return ret


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.degree = 0
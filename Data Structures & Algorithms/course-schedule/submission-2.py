class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [Node(i) for i in range(numCourses)]
        roots = set([i for i in range(numCourses)])
        for pre in prerequisites:
            before, after = pre[1], pre[0]
            if before == after:
                return False
            roots.discard(after)
            nodes[before].children.append(nodes[after])

        def search(node):
            nonlocal triversed
            if node.val in triversed:
                return False
            triversed.add(node.val)
            for child in node.children:
                if search(child) == False:
                    return False
            triversed.remove(node.val)
            return True
        
        if len(roots) == 0:
            return False
        for r in roots:
            root = nodes[r]
            triversed = set()
            if search(root) == False:
                return False
        return True


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
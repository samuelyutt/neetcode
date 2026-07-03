"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        nodes = {node.val: Node(node.val)}
        visited = set([node.val])
        q = deque([node])

        while q:
            node = q.popleft()
            my_node = nodes[node.val]

            for nei in node.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                
                my_node.neighbors.append(nodes[nei.val])

                if nei.val not in visited:
                    visited.add(nei.val)
                    q.append(nei)

        return nodes[1]


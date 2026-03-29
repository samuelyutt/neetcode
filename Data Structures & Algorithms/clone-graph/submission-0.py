"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_nodes = {1: Node(1)}
        traversed = set()

        def traverse(node):
            if node.val in traversed:
                return
            traversed.add(node.val)
            my_node = my_nodes[node.val]
            for neighbor in node.neighbors:
                if neighbor.val not in my_nodes:
                    my_nodes[neighbor.val] = Node(neighbor.val)
                my_node.neighbors.append(my_nodes[neighbor.val])
                traverse(neighbor)

        if node is None:
            return None
        traverse(node)
        return my_nodes[1]
                
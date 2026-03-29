"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.my_nodes = {}

        node = head
        while node:
            self.my_nodes[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            if node.next:
                self.my_nodes[node].next = self.my_nodes[node.next]
            if node.random:
                self.my_nodes[node].random = self.my_nodes[node.random]
            node = node.next

        return self.my_nodes[head] if head else None
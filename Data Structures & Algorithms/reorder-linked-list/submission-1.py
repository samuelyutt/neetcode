# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next

        n = len(nodes)

        inc = [i for i in range(n)]
        dec = [i for i in range(n - 1, -1, -1)]

        reordered_nodes = []

        print(inc,dec)

        for a, b in zip(inc[:n // 2], dec[:n // 2]):
            reordered_nodes.append(nodes[a])
            reordered_nodes.append(nodes[b])

        if n % 2:
            reordered_nodes.append(nodes[n // 2])

        for i in range(1, n):
            reordered_nodes[i - 1].next = reordered_nodes[i]

        reordered_nodes[-1].next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i, node in enumerate(lists):
            heapq.heappush(q, (node.val, i, node))

        head, prev = None, None
        while q:
            _, i, node = heapq.heappop(q)
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
            node.next = None
            if prev:
                prev.next = node
            else:
                head = node
            prev = node

        return head
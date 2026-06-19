# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(h, (node.val, i))
        
        head = None
        prev = None

        while h:
            _, i = heapq.heappop(h)

            node = lists[i]

            if head is None:
                head = node

            if prev:
                prev.next = node

            prev = node

            if node.next:
                heapq.heappush(h, (node.next.val, i))
                lists[i] = lists[i].next

        if prev:
            prev.next = None

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        
        of = 0
        prev, head = None, None
        while l1 or l2:
            sum = of
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            node = ListNode(sum % 10)
            if head is None:
                head = node
            if prev:
                prev.next = node
            prev = node
            of = sum // 10

        if of:
            node = ListNode(of)
            if head is None:
                head = node
            if prev:
                prev.next = node

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n, node = 0, head
        while node:
            n += 1
            node = node.next

        back = head
        for i in range(n // 2):
            back = back.next

        prev_back, back_head = None, None
        while back:
            back_head= back
            next = back.next
            back.next = prev_back
            back, prev_back = next, back

        front, back = head, back_head
        prev = None
        for i in range(n // 2):
            if prev:
                prev.next = front
            prev = front
            front = front.next

            prev.next = back
            prev = back
            if back:
                back = back.next
        if n % 2:
            if prev:
                prev.next = front
            front.next = None

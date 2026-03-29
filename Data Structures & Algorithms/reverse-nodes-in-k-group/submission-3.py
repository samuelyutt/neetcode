# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        segs = []
        new_head = None

        while True:
            segs.append(slow)
            for i in range(k - 1):
                if fast:
                    fast = fast.next
                else:
                    break
            if fast is None:
                if len(segs) > 1:
                    segs.pop(0).next = slow
                break
            else:
                tmp = fast.next
                prev = None
                while True:

                    if slow == fast:
                        slow.next = prev
                        if len(segs) > 1:
                            segs.pop(0).next = slow
                        if new_head is None:
                            new_head = slow
                        break
                    next = slow.next
                    slow.next = prev
                    prev = slow
                    slow = next

                slow = fast = tmp

        return new_head
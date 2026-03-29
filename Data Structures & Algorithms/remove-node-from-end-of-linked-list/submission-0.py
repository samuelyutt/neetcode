# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_slow, slow, fast = None, head, head

        for _ in range(n - 1):
            fast = fast.next
        
        while fast.next:
            prev_slow, slow = slow, slow.next
            fast = fast.next

        if prev_slow is None:
            if slow:
                return slow.next
            else:
                return None
        else:
            prev_slow.next = slow.next
            return head

        
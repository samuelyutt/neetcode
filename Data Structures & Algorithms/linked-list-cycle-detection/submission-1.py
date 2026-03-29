# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while True:
            for i in range(2):
                if fast is None:
                    return False
                fast = fast.next
                if fast == slow:
                    return True
            slow = slow.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(v1, v2):
            if v2 > v1:
                v1, v2 = v2, v1
            
            while v2:
                v1 = v1 % v2
                v1, v2 = v2, v1

            return v1

        left, right = head, head.next
        while right:
            node = ListNode(gcd(left.val, right.val), right)
            left.next = node

            left, right = right, right.next

        return head
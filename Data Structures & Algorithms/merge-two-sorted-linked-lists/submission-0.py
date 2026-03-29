# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev, head = None, None

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node = ListNode(list1.val)
                    list1 = list1.next
                else:
                    node = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next

            if prev:
                prev.next = node
            if not head:
                head = node
            prev = node

        return head
        

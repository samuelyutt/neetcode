# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # A -> a -> . -> b -> B
        # A ------------->
        #      a <- . <- b
        #      -------------> B

        if left == right:
            return head

        prev, node = None, head
        idx = 1
        while node:
            if idx == left:
                node_A = prev
                node_a = node
            elif idx == right:
                node_B = node.next
                node_b = node
                break
            prev, node = node, node.next
            idx += 1
        
        prev, node = node_a, node_a.next

        while node:
            # prev, node, node.next = node, node.next, prev
            tmp = node.next
            node.next = prev
            prev, node = node, tmp

            if prev == node_b:
                break

        
        if node_A:
            node_A.next = node_b
        else:
            head = node_b
        node_a.next = node_B

        return head

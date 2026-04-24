# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev, node = None, root
        while node:
            if node.val == key:
                # get next node
                next = None
                if node.left:
                    next = node.left
                elif node.right:
                    next = node.right

                # delete this node
                if prev:
                    if node.val < prev.val:
                        prev.left = next
                    else:
                        prev.right = next
                else:
                    root = next

                # append orphan node
                if node.left and node.right:
                    orphan = node.right
                    node = root
                    while node:
                        if orphan.val < node.val:
                            if node.left is None:
                                node.left = orphan
                                break
                            else:
                                node = node.left
                        else:
                            if node.right is None:
                                node.right = orphan
                                break
                            else:
                                node = node.right

                break

            elif key < node.val:
                # go left
                prev, node = node, node.left

            elif key > node.val:
                # go right
                prev, node = node, node.right

        return root
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertNode(root)
        return root

    def invertNode(self, node):
        if node and (node.left or node.right):
            node.left, node.right = node.right, node.left
            self.invertNode(node.left)
            self.invertNode(node.right)
            return
        else:
            return
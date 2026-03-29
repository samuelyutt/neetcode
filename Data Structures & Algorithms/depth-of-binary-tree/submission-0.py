# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.findMaxDepth(root, 1)

    def findMaxDepth(self, node, cur_depth) -> int:
        return max(
            self.findMaxDepth(node.left, cur_depth + 1) if node.left else cur_depth,
            self.findMaxDepth(node.right, cur_depth + 1) if node.right else cur_depth,
        )
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            if not node.left:
                return [node.val] + traverse(node.right)
            if not node.right:
                return traverse(node.left) + [node.val]
            return traverse(node.left) + [node.val] + traverse(node.right)

        return traverse(root)

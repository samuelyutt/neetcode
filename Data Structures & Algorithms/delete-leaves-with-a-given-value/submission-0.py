# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None

        def traverse(node, parent, side):
            if node.left:
                traverse(node.left, node, 'left')
            if node.right:
                traverse(node.right, node, 'right')
            
            if not node.left and not node.right and node.val == target:
                # delete this node
                if parent:
                    setattr(parent, side, None)

        traverse(root, None, None)
        return root if root.left or root.right or root.val != target else None
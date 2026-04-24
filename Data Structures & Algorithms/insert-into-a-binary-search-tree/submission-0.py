# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def traverse(node):
            if val < node.val:
                # go left
                if node.left:
                    traverse(node.left)
                else:
                    new_node = TreeNode(val)
                    node.left = new_node
            elif node.val < val:
                # go right
                r = val
                if node.right:
                    traverse(node.right)
                else:
                    new_node = TreeNode(val)
                    node.right = new_node

        if root is None:
            return TreeNode(val)
        traverse(root)        
        return root
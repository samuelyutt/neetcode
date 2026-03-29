# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -1001

        def search(node):
            if node is None:
                return 0
            l = search(node.left)
            r = search(node.right)
            self.ret = max(self.ret, node.val, l + node.val, r + node.val, l + r + node.val)
            return max(node.val, l + node.val, r + node.val)

        search(root)
        return self.ret
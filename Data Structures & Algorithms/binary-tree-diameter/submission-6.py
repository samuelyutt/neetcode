# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ret = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.findDepth(root, 1)
        return self.ret
    
    def findDepth(self, node, cur_depth) -> int:
        a = self.findDepth(node.left, cur_depth + 1) if node.left else cur_depth
        b = self.findDepth(node.right, cur_depth + 1) if node.right else cur_depth
        max_depth = max(a, b)
        self.ret = max(self.ret, cur_depth - 1, a - cur_depth + b - cur_depth)
        return max_depth
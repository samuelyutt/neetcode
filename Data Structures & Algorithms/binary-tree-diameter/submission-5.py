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
        # global ret
        print(self.ret)
        a = self.findDepth(node.left, cur_depth + 1) if node.left else cur_depth
        b = self.findDepth(node.right, cur_depth + 1) if node.right else cur_depth
        max_depth = max(a, b)
        print(cur_depth, a, b, self.ret, cur_depth - 1, a - cur_depth + b - cur_depth)
        self.ret = max(self.ret, cur_depth - 1, a - cur_depth + b - cur_depth)
        print(node.val, self.ret)
        return max_depth
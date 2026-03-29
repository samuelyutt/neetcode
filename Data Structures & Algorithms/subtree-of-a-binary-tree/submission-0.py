# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.subRoot = None

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRoot = subRoot
        return self.triverse(root)

    def triverse(self, node):
        if node is None:
            return False
        if self.check(node, self.subRoot):
            return True
        return self.triverse(node.left) or self.triverse(node.right)

    def check(self, a, b):
        if a is None != b is None:
            return False
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return self.check(a.left, b.left) and self.check(a.right, b.right)
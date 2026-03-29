# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p, q)       

    def compare(self, a, b):
        if a and b:
            return a.val == b.val and self.compare(a.left, b.left) and self.compare(a.right, b.right)
        elif a is None and b is None:
            return True
        else:
            return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ret = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.ret = 0
        self.triverse(root, -101)
        return self.ret

    def triverse(self, node, val):
        if node is None:
            return

        if node.val >= val:
            self.ret += 1

        self.triverse(node.left, max(val, node.val))
        self.triverse(node.right, max(val, node.val))
        
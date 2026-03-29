# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#    5
#  1   4
# x x 3 6
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.triverse(root)[0]

    def triverse(self, node):
        if node.left:
            ret_l, max_l, min_l = self.triverse(node.left)
        if node.right:
            ret_r, max_r, min_r = self.triverse(node.right)

        if node.left and node.right:
            return ret_l and ret_r and max_l < node.val < min_r, max(node.val, max_l, max_r), min(node.val, min_l, min_r)
        elif node.left:
            return ret_l and max_l < node.val, max(node.val, max_l), min(node.val, min_l)
        elif node.right:
            return ret_r and node.val < min_r, max(node.val, max_r), min(node.val, min_r)
        else:
            return True, node.val, node.val
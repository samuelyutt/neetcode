# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

ret = None

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global ret
        ret = True
        if root is None:
            return True
        self.calHeight(root, 1)
        return ret

    def calHeight(self, node, cur_height) -> int:
        global ret
        if ret == False:
            return -1

        a = self.calHeight(node.left, cur_height + 1) if node.left else cur_height
        b = self.calHeight(node.right, cur_height + 1) if node.right else cur_height

        if abs(a - b) > 1:
            ret = False
            return -1
        
        return max(a, b)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ret = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.triverse(root, 0)
        return self.ret

    def triverse(self, node, level):
        if node is None:
            return

        if level > len(self.ret) - 1:
            self.ret.append(node.val)
        
        self.ret[level] = node.val
        self.triverse(node.left, level + 1)
        self.triverse(node.right, level + 1)
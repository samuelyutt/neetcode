# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.k = None
        self.ret = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ret = None
        self.triverse(root, 0)
        return self.ret.val
        
    def triverse(self, node, cnt):
        if self.ret:
            return -1

        if node.left:
            cnt = self.triverse(node.left, cnt)

        cnt += 1
        if cnt == self.k:
            self.ret = node
        
        if self.ret:
            return -1

        if node.right:
            cnt = self.triverse(node.right, cnt)

        return cnt
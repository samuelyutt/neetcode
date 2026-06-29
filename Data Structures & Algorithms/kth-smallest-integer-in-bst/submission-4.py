# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ret = None

        def search(node):
            if node.left:
                search(node.left)

            nonlocal cnt, ret
            cnt += 1
            if cnt == k:
                ret = node.val

            if node.right:
                search(node.right)

        search(root)

        return ret
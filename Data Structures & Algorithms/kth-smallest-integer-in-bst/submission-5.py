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
            nonlocal cnt, ret
            
            if not node or ret:
                return

            search(node.left)

            cnt += 1
            if cnt == k:
                ret = node.val

            search(node.right)

        search(root)

        return ret
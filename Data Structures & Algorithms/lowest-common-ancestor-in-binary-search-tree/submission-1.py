# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ret = None

        def search(node):
            nonlocal ret

            above_p, above_q = False, False

            if node.val == p.val:
                above_p = True
            
            if node.val == q.val:
                above_q = True

            if node.left:
                a, b = search(node.left)
                above_p |= a
                above_q |= b

            if node.right:
                a, b = search(node.right)
                above_p |= a
                above_q |= b
            
            if above_p and above_q and ret is None:
                ret = node

            return above_p, above_q

        search(root)

        return ret

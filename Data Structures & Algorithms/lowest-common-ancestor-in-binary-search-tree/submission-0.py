# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.ret = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p
        self.q = q
        self.ret = None
        self.find(root)
        return self.ret

    def find(self, node):
        if node is None:
            return False, False

        p_in_left, q_in_left = self.find(node.left)
        p_in_right, q_in_right = self.find(node.right)

        if self.ret is not None:
            return True, True

        p_found = p_in_left or p_in_right or node.val == self.p.val
        q_found = q_in_left or q_in_right or node.val == self.q.val

        if p_found and q_found:
            self.ret = node

        return p_found, q_found

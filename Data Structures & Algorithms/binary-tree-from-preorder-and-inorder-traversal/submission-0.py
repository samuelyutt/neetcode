# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        nodes = {} # val -> idx of inorder, Node
        for idx, val in enumerate(inorder):
            nodes[val] = (idx, TreeNode(val))

        def construct(l, r):
            val = preorder[self.i]
            m, node = nodes[val]
            self.i += 1
            if l < m:
                node.left = construct(l, m - 1)
            if m < r:
                node.right = construct(m + 1, r)
            return node

        return construct(0, len(nodes) - 1)
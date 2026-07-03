# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodes = {val: (TreeNode(val), i) for i, val in enumerate(inorder)}
        i = 0

        def search(l, r):
            if l > r:
                return None

            nonlocal i

            val = preorder[i]
            node, m = nodes[val]

            i += 1

            node.left = search(l, m - 1)
            node.right = search(m + 1, r)

            return node

        return search(0, len(preorder) - 1)

            
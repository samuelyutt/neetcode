# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ret = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal(root, 0)
        return self.ret

    def traversal(self, node, cur_level):
        if node is None:
            return

        if len(self.ret) <= cur_level:
            self.ret.append([])

        self.ret[cur_level] += [node.val]

        if node.left:
            self.traversal(node.left, cur_level + 1)
        if node.right:
            self.traversal(node.right, cur_level + 1)

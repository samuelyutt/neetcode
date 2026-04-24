# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def traverse(node):
            if not node.left and not node.right:
                return node.val, 0  # rob this, not rob this
            elif not node.right:
                rob_next, not_rob_next = traverse(node.left)
                return (
                    node.val + not_rob_next, # rob this
                    max(rob_next, not_rob_next),  #  not rob this
                )
            elif not node.left:
                rob_next, not_rob_next = traverse(node.right)
                return (
                    node.val + not_rob_next, # rob this
                    max(rob_next, not_rob_next),  #  not rob this
                )
            else:
                rob_left, not_rob_left = traverse(node.left)
                rob_right, not_rob_right = traverse(node.right)
                return (
                    node.val + not_rob_left + not_rob_right, # rob this
                    max(
                        rob_left + rob_right,
                        not_rob_left + rob_right,
                        rob_left + not_rob_right,
                        not_rob_left + not_rob_right,
                    ), # not rob this
                )

        return max(traverse(root))

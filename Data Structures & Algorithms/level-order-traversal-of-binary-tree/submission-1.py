# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q, new_q = deque(), deque([root])
        ret = []

        while new_q:
            q, new_q = new_q, deque()
            level = []

            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            
            ret.append(level)
        
        return ret
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        def triverse(node) -> list:
            if node is None:
                return ['x']
            nonlocal ret
            ret = ([str(node.val)] + triverse(node.left) + triverse(node.right) + ['#'])
            return ret
        ret = triverse(root)
        return ' '.join(ret)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        tokens = data.split()
        stack = []
        for t in tokens:
            if t == '#':
                right = stack.pop()
                left = stack.pop()
                node = stack.pop()
                node.left = left
                node.right = right
                stack.append(node)
            elif t == 'x':
                stack.append(None)
            else:
                stack.append(TreeNode(int(t)))
            print(t, stack)
        return stack[0]

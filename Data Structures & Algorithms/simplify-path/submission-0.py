class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item == '.':
                pass
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                if item:
                    stack.append(item)
        return '/' + '/'.join(stack)
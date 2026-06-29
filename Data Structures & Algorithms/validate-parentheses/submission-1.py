class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for c in s:
            if c in p:
                stack.append(p[c])
            else:
                if len(stack) == 0 or stack[-1] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0
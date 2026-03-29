class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for c in s:
            if c in m:
                # left chars
                stack.append(m[c])
            else:
                # right chars
                if len(stack) == 0:
                    return False
                if stack[-1] == c:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

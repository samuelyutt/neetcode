class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                # extract string part
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                num = ''
                stack.pop()

                # extract number part
                while stack and len(stack[-1]) == 1 and 0 <= ord(stack[-1]) - ord('0') <= 9:
                    num = stack.pop() + num
                if not num:
                    num = 1
                stack.append(tmp * int(num))
            else:
                stack.append(c)

        return ''.join(stack)
        
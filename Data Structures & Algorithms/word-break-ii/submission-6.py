class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # build tree
        root = Node(None)
        for word in wordDict:
            node = root
            for c in word:
                if node.childs[ord(c) - ord('a')] is None:
                    node.childs[ord(c) - ord('a')] = Node(c)
                node = node.childs[ord(c) - ord('a')]
            node.word = word

        # traverse
        ret = []
        cur = []
        i = 0

        def search(node):
            nonlocal ret, cur, i

            if node.word:
                cur.append(node.word)
                if i == len(s):
                    ret.append(' '.join(cur))
                else:
                    search(root)
                cur.pop()

            if i == len(s):
                return

            if not 0 <= ord(s[i]) - ord('a') < 26:
                return

            next = node.childs[ord(s[i]) - ord('a')]
            if next is not None:
                i += 1
                search(next)
                i -= 1

        search(root)
        return ret


class Node:
    def __init__(self, val):
        self.val = val
        self.word = None
        self.childs = [None] * 26
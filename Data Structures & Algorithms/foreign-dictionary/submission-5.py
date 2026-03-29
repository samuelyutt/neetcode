class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        tree = Tree(words)
        rules = {} # c -> set([a, b])

        if tree.fail:
            return ''

        def dfs(node):
            nonlocal rules
            keys = list(node.children.keys())
            for c in keys:
                if c not in rules:
                    rules[c] = set()
            for i, c in enumerate(keys[1:], 1):
                rules[c].add(keys[i - 1])
            for c, child in node.children.items():
                dfs(child)
        dfs(tree.root)

        added = set()
        ret = []

        while len(added) < len(rules):
            cnt = 0
            for c in rules:
                if c in added:
                    continue
                if len(rules[c]) != 0:
                    continue
                added.add(c)
                ret.append(c)
                cnt += 1
                for x in rules:
                    rules[x].discard(c)
            if cnt == 0:
                return ''

        return ''.join(ret)


class Tree:
    def __init__(self, words):
        self.root = Node(None)
        self.fail = False
        prev = None
        for word in words:
            if word == prev:
                continue
            self.add(word)
            prev = word

    def add(self, word):
        node = self.root
        i = 0
        while i < len(word):
            c = word[i]
            if c not in node.children:
                node.children[c] = Node(c)
            else:
                if i == len(word) - 1:
                    self.fail = True
            if c != list(node.children.keys())[-1]:
                self.fail = True
            node = node.children[c]
            i += 1


class Node:
    def __init__(self, val):
        self.children = OrderedDict()
        self.val = val

class Node:
    def __init__(self):
        self.d = defaultdict(Node)


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        word += '#'
        def _add(node, i):
            if i >= len(word):
                return
            char = word[i]
            _add(node.d[char], i + 1)
        _add(self.root, 0)

    def search(self, word: str) -> bool:
        word += '#'
        def _search(node, i):
            if i >= len(word):
                return True
            char = word[i]
            if char == '.':
                for c in node.d:
                    if (_search(node.d[c], i + 1)):
                        return True
                return False
            elif char in node.d:
                return _search(node.d[char], i + 1)
            else:
                return False
        return _search(self.root, 0)

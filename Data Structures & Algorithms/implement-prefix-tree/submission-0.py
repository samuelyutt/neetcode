class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        word += '#'
        def _insert(node, i):
            if i >= len(word):
                return
            char = word[i]
            _insert(node.d[char], i + 1)
        _insert(self.root, 0)

    def search(self, word: str) -> bool:
        word += '#'
        def _search(node, i):
            if i >= len(word):
                return True
            char = word[i]
            if char in node.d:
                return _search(node.d[char], i + 1)
            else:
                return False
        return _search(self.root, 0)

    def startsWith(self, prefix: str) -> bool:
        def _search(node, i):
            if i >= len(prefix):
                return True
            char = prefix[i]
            if char in node.d:
                return _search(node.d[char], i + 1)
            else:
                return False
        return _search(self.root, 0)
 
class Node:
    def __init__(self):
        self.d = defaultdict(Node)
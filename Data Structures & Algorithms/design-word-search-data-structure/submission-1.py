class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end
            
            if word[i] == '.':
                for c, child in node.children.items():
                    if dfs(i + 1, child):
                        return True
                return False

            elif word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])

            else:
                return False

        return dfs(0, self.root)


class Node:

    def __init__(self):
        self.children = {}
        self.is_end = False
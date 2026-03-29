class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = TrieTree(words)
        ret = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, node):
            if not 0 <= i < len(board) or not 0 <= j < len(board[i]):
                return
            if node is None:
                return
            if node.remain == 0:
                return
            if node.word:
                ret.append(node.word)
                node.word = None
                node.remain -= 1

            board[i][j], tmp = '*', board[i][j]
            for dir in dirs:
                x, y = i + dir[0], j + dir[1]
                if not 0 <= x < len(board) or not 0 <= y < len(board[x]):
                    continue
                if not 0 <= ord(board[x][y]) - ord('a') < 26:
                    continue
                dfs(x, y, node.children[ord(board[x][y]) - ord('a')])
            board[i][j] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, tree.root.children[ord(board[i][j]) - ord('a')])
        return ret


class TrieTree:
    def __init__(self, words):
        self.root = Node(None)
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if node.children[ord(c) - ord('a')] is None:
                node.children[ord(c) - ord('a')] = Node(c)
            next_node = node.children[ord(c) - ord('a')]
            next_node.remain += 1
            if i == len(word) - 1:
                next_node.word = word
            node = next_node

class Node:
    def __init__(self, val):
        self.children = [None] * 26
        self.remain = 0
        self.val = val
        self.word = None
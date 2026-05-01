class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        
        root = Node(None)
        for word in words:
            node = root
            for c in word:
                val = d[c]
                if not node.childs or node.childs[-1].val < val:
                    # new child node
                    node.childs.append(Node(val))
                    node = node.childs[-1]
                elif node.childs[-1].val == val:
                    # child node already exist
                    node = node.childs[-1]
                else:
                    # not in order
                    return False
            if node.childs:
                return False
        
        return True

        

class Node:
    def __init__(self, val):
        self.val = val
        self.childs = []
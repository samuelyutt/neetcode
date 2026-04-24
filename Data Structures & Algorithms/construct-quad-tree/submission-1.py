"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        memo = {} # (x, y, side) -> Node
        for i in range(n):
            for j in range(n):
                memo[(i, j, 1)] = Node(grid[i][j], 1, None, None, None, None)

        side = 1
        while side < n:
            next_side = side * 2
            for i in range(0, n, next_side):
                for j in range(0, n, next_side):
                    tl = memo[(i, j, side)]
                    tr = memo[(i, j + side, side)]
                    bl = memo[(i + side, j, side)]
                    br = memo[(i + side, j + side, side)]
                    sum_val = sum([tl.val, tr.val, bl.val, br.val])
                    all_leaf = sum([tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf]) == 4
                    if all_leaf and (sum_val == 0 or sum_val == 4):
                        memo[(i, j, next_side)] = Node(tl.val, 1, None, None, None, None)
                        del memo[(i, j, side)]
                        del memo[(i, j + side, side)]
                        del memo[(i + side, j, side)]
                        del memo[(i + side, j + side, side)]
                    else:
                        memo[(i, j, next_side)] = Node(1, 0, tl, tr, bl, br)
            side = next_side

        return memo[(0, 0, n)]


                    

                    
                    
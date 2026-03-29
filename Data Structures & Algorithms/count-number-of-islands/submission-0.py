class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    lands.add((i, j))

        def search(x, y):
            if (x, y) not in lands:
                return
            lands.remove((x, y))
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)

        ret = 0
        while lands:
            ret += 1
            x, y = lands.pop()
            lands.add((x, y))
            search(x, y)
        return ret
                        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    lands.add((i, j))

        ret, cur_area = 0, 0

        def search(x, y):
            if (x, y) not in lands:
                return
            nonlocal ret, cur_area
            cur_area += 1
            ret = max(cur_area, ret)
            lands.remove((x, y))
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)

        while lands:
            cur_area = 0
            x, y = lands.pop()
            lands.add((x, y))
            search(x, y)
        return ret
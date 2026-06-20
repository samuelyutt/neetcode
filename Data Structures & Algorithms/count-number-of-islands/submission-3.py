class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cells = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    cells.add((i, j))

        ret = 0
        while cells:
            ret += 1

            q = deque([cells.pop()])
            while q:
                i, j = q.popleft()
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (i + x, j + y) in cells:
                        cells.remove((i + x, j + y))
                        q.append((i + x, j + y))

        return ret
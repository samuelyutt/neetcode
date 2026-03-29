class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def search(i, j, dist):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]):
                return
            if grid[i][j] == -1:
                return
            if grid[i][j] < dist:
                return
            grid[i][j] = dist
            search(i + 1, j, dist + 1)
            search(i - 1, j, dist + 1)
            search(i, j + 1, dist + 1)
            search(i, j - 1, dist + 1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    search(i, j, 0)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ret += 4
                    if i and grid[i - 1][j]:
                        ret -= 2
                    if j and grid[i][j - 1]:
                        ret -= 2
        return ret
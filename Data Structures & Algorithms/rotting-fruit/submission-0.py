class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] -= 2

        # 0 -> rotton
        # -1 -> fresh
        # -2 -> empty

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q = deque([
                        (i + 1, j, 1),
                        (i - 1, j, 1),
                        (i, j + 1, 1),
                        (i, j - 1, 1),
                    ])
                    while q:
                        x, y, step = q.popleft()
                        if not 0 <= x < len(grid) or not 0 <= y < len(grid[x]):
                            continue
                        if grid[x][y] == -1 or grid[x][y] > step:
                            grid[x][y] = step
                            q.append((x + 1, y, step + 1))
                            q.append((x - 1, y, step + 1))
                            q.append((x, y + 1, step + 1))
                            q.append((x, y - 1, step + 1))

        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == -1:
                    return -1
                elif grid[i][j] > 0:
                    ret = max(ret, grid[i][j])
        return ret
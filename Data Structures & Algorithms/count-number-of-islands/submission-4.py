class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    lands.add((i, j))

        ret = 0

        while lands:
            ret += 1

            q = deque([lands.pop()])
            while q:
                x, y = q.popleft()

                for a, b in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if (x + a, y + b) in lands:
                        lands.remove((x + a, y + b))
                        q.append((x + a, y + b))
        
        return ret
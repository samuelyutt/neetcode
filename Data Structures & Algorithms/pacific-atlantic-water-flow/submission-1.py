class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pac = set()
        q = deque()

        for i in range(m):
            q.append((i, 0))
        for j in range(n):
            q.append((0, j))

        while q:
            x, y = q.popleft()
            if (x, y) in pac:
                continue
            
            pac.add((x, y))
            
            for a, b in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
                if (a, b) in pac:
                    continue
                if not 0 <= a < m or not 0 <= b < n:
                    continue
                if heights[a][b] < heights[x][y]:
                    continue
                q.append((a, b))

        atl = set()
        q = deque()

        for i in range(m):
            q.append((i, n - 1))
        for j in range(n):
            q.append((m - 1, j))

        while q:
            x, y = q.popleft()
            if (x, y) in atl:
                continue
            
            atl.add((x, y))
            
            for a, b in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
                if (a, b) in atl:
                    continue
                if not 0 <= a < m or not 0 <= b < n:
                    continue
                if heights[a][b] < heights[x][y]:
                    continue
                q.append((a, b))

        ret = []
        for x, y in pac:
            if (x, y) in atl:
                ret.append((x, y))
        return ret
                
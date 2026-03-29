class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        w, h = len(heights[0]), len(heights)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        pacific = set()
        q = deque([(0, j) for j in range(w)] + [(i, 0) for i in range(h)])
        while q:
            x, y = q.popleft()
            if not 0 <= x < h or not 0 <= y < w:
                continue
            if (x, y) in pacific:
                continue
            pacific.add((x, y))
            for m, n in dirs:
                x_p, y_p = x + m, y + n
                if 0 <= x_p < h and 0 <= y_p < w and heights[x][y] <= heights[x_p][y_p]:
                    q.append((x_p, y_p))

        atlantic = set()
        q = deque([(h - 1, j) for j in range(w)] + [(i, w - 1) for i in range(h)])
        while q:
            x, y = q.popleft()
            if not 0 <= x < h or not 0 <= y < w:
                continue
            if (x, y) in atlantic:
                continue
            atlantic.add((x, y))
            for m, n in dirs:
                x_p, y_p = x + m, y + n
                if 0 <= x_p < h and 0 <= y_p < w and heights[x][y] <= heights[x_p][y_p]:
                    q.append((x_p, y_p))

        ret = []
        for x, y in pacific:
            if (x, y) in atlantic:
                ret.append([x, y])
        return ret
            
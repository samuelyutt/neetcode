class CountSquares:

    def __init__(self):
        self.axis_x = {}
        self.axis_y = {}

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]

        if x not in self.axis_x:
            self.axis_x[x] = {y: 0}
        elif y not in self.axis_x[x]:
            self.axis_x[x][y] = 0
        self.axis_x[x][y] += 1

        if y not in self.axis_y:
            self.axis_y[y] = {x: 0}
        elif x not in self.axis_y[y]:
            self.axis_y[y][x] = 0
        self.axis_y[y][x] += 1

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]

        ret = 0
        for y, cnt2 in self.axis_x.get(px, {}).items():
            if py == y:
                continue
            for x, cnt1 in self.axis_y.get(py, {}).items():
                if px == x:
                    continue
                cnt3 = self.axis_x.get(x, {}).get(y, 0)
                ret += cnt1 * cnt2 * cnt3
        
        return ret


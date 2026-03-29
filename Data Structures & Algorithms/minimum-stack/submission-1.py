class MinStack:

    def __init__(self):
        self.l = []
        self.min_l = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.min_l) == 0 or val < self.min_l[-1]:
            self.min_l.append(val)
        else:
            self.min_l.append(self.min_l[-1])

    def pop(self) -> None:
        self.l = self.l[:len(self.l) - 1]
        self.min_l = self.min_l[:len(self.min_l) - 1]

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min_l[-1]

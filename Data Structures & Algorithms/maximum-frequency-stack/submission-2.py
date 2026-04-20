class FreqStack:

    def __init__(self):
        self.hist = defaultdict(list) # val -> [idx]
        self.i = 0
        self.max_cnt = 0
        self.next_pop = None

    def push(self, val: int) -> None:
        self.hist[val].append(self.i)
        if len(self.hist[val]) >= self.max_cnt:
            self.max_cnt = len(self.hist[val])
            self.next_pop = val
        self.i += 1

    def pop(self) -> int:
        ret = self.next_pop
        self.hist[ret].pop()
        if len(self.hist[ret]) == 0:
            del self.hist[ret]

        self.max_cnt = 0
        self.next_pop = None
        max_idx = -1
        for val in self.hist:
            if len(self.hist[val]) >= self.max_cnt and self.hist[val][-1] > max_idx:
                self.max_cnt = len(self.hist[val])
                self.next_pop = val
                max_idx = self.hist[val][-1]
        
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
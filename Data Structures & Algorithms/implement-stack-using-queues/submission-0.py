class MyStack:
    # [1] + 2
    # [2 1] + 3
    # [3 2 1]
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        tmp = deque()
        tmp.append(x)
        while self.q:
            tmp.append(self.q.popleft())
        self.q = tmp

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
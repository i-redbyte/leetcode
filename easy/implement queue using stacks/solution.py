from collections import deque


class MyQueue:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        return self.d.popleft()

    def peek(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        return not self.d


obj = MyQueue()
obj.push(222)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

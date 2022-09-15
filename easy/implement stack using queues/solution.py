class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        top = self.queue[-1]
        self.queue = self.queue[:-1]
        return top

    def top(self) -> int:
        if len(self.queue) == 0:
            return None
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
x = 123
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

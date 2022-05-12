class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.getMin())))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


minStack = MinStack()
print(minStack.push(2147483646))
print(minStack.push(2147483646))
print(minStack.push(2147483647))
print(minStack.stack)
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
print(minStack.pop())
print(minStack.stack)
print(minStack.push(2147483647))
print(minStack.top())
print(minStack.getMin())
print(minStack.push(-2147483648))
print(minStack.top())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # return -3
# minStack.pop()
# print(minStack.top())  # return 0
# print(minStack.getMin())  # return -2

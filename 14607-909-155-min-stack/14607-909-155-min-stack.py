import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.increasing = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals or self.minVals[-1] >= val:
            self.minVals.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minVals[-1] == val:
            self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
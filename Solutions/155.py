class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.data.append(x)
        self.min = min(self.min, x)

    def pop(self) -> None:
        val = self.data.pop()
        if val == self.min:
            self.min = self._min()

    def top(self) -> int:
        val = self.data[-1]
        return val

    def getMin(self) -> int:
        return self.min

    def _min(self):
        if not self.data:
            return float('inf')
        else:
            return min(self.data)


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2

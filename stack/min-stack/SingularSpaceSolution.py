class MinStackSpaceConstraint:

    def __init__(self):
        self.stack = []
        self.minValue = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.minValue = val
            self.stack.append(val)
        else:
            if val < self.minValue:
                # 2*ele - minEle should be pushed.
                modifiedVal = 2 * val - self.minValue
                self.minValue = val
                self.stack.append(modifiedVal)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] < self.minValue:
            self.minValue = 2*self.minValue - self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < self.minValue:
            return self.minValue
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue

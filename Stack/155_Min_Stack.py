class MinStack:

    def __init__(self):
        #delcaring a stack to store the pushed ele
        self.stack = []
        #minimum val
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #finding the minimum value between val and the top of minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
            return
        tmp = []
        while self.minStack and self.minStack[-1] < val:
            tmp.append(self.minStack[-1])
            self.minStack.pop()
        self.minStack.append(val)
        while tmp:
            self.minStack.append(tmp[-1])
            tmp.pop()

    def pop(self) -> None:
        val = self.stack[-1]
        self.stack.pop()
        tmp = []
        while self.minStack[-1] != val:
            tmp.append(self.minStack[-1])
            self.minStack.pop()
        self.minStack.pop()
        while tmp:
            self.minStack.append(tmp[-1])
            tmp.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

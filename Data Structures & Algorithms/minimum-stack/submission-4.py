class MinStack:
    # 2 stacks . keeping track of minimum
    def __init__(self):
        self.minn = float('inf')
        self.mS = []
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.minn = min(self.minn, val)      
        self.mS.append(self.minn)

    def pop(self) -> None:
        self.s.pop()
        self.mS.pop()
        self.minn = self.mS[-1] if self.mS else float('inf')

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mS[-1]

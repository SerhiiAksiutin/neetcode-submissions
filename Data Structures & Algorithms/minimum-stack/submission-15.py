class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mini = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # self.stack_mini.append(min(self.stack_mini[-1], val) if self.stack_mini else val)
        if self.stack_mini:
            self.stack_mini.append(min(self.stack_mini[-1], val))
        else:
            self.stack_mini.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mini.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_mini[-1]
        



class MinStack:

    def __init__(self):
        self.stack = [] #LIFO

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minStack = [self.stack[-1]]
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] < minStack[0]:
                minStack[0] = self.stack[i]
        return minStack[0]

        

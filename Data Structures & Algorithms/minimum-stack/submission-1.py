class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # position of the current min
        
    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[self.minstack[-1]]:
            # latest element added becomes the min
            self.minstack.append(len(self.stack))
        else:
            # current remains min.
            self.minstack.append(self.minstack[-1])

        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
        

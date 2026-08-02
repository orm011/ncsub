from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque() 
        
    def push(self, x: int) -> None:
        # only one is used at a time.
        if not self.q2:
            self.q1.append(x)
        else:
            self.q2.append(x)
        
    def _poptophelper(self, mode: str) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            top = self.q1.pop()
            if mode == "top":
                self.q2.append(top)
        elif self.q2:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            top =  self.q2.pop()
            if mode == "top":
                self.q1.append(top)

        return top

    def pop(self) -> int:
        return self._poptophelper("pop")

    def top(self) -> int:
        return self._poptophelper("top")

    def empty(self) -> bool:
        return not (self.q1 or self.q2)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_ = val
        else:
            self.stack.append(val - self.min_)
            if val < self.min_:
                self.min_ = val

    def pop(self) -> None:
        encoded = self.stack.pop()
        if encoded < 0: # has been updated
            self.min_ -= encoded


    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_
        
        return self.stack[-1] + self.min_
        

    def getMin(self) -> int:
        return self.min_

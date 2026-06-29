class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        val = min(val, self.minArr[-1] if self.minArr else val)
        self.minArr.append(val)


    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minArr[-1] 

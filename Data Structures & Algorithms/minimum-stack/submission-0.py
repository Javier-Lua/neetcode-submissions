class MinStack:
    # Create two stacks, one for the normal stack
    # the other to keep track of history of min values

    def __init__(self):
        self.stackMain = []
        self.stackHist = []

    def push(self, val: int) -> None:
        self.stackMain.append(val)
        if self.stackHist:
            curr_min = self.stackHist[-1]
            if val <= curr_min:
                self.stackHist.append(val)
        else:
            self.stackHist.append(val)

    def pop(self) -> None:
        ele = self.stackMain.pop()
        if self.stackHist[-1] == ele:
            self.stackHist.pop()

    def top(self) -> int:
        return self.stackMain[-1]

    def getMin(self) -> int:
        return self.stackHist[-1]

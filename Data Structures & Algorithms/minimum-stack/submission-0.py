class MinStack:

    def __init__(self):
        self.differences = []
        self.minimum = None

    def push(self, val: int) -> None:
        if not self.differences:
            self.differences.append(0)
            self.minimum = val
            return

        self.differences.append(val - self.minimum)

        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        difference = self.differences.pop()

        if difference < 0:
            self.minimum = self.minimum - difference

    def top(self) -> int:
        difference = self.differences[-1]

        if difference < 0:
            return self.minimum

        return self.minimum + difference

    def getMin(self) -> int:
        return self.minimum
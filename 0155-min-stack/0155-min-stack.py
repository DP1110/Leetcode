class MinStack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, v):
        self.s.append(v)
        mn = v if not self.m else min(v, self.m[-1])
        self.m.append(mn)

    def pop(self):
        self.s.pop()
        self.m.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.m[-1]
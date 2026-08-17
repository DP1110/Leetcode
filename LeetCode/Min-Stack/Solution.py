1class MinStack:
2    def __init__(self):
3        self.s = []
4        self.m = []
5
6    def push(self, v):
7        self.s.append(v)
8        mn = v if not self.m else min(v, self.m[-1])
9        self.m.append(mn)
10
11    def pop(self):
12        self.s.pop()
13        self.m.pop()
14
15    def top(self):
16        return self.s[-1]
17
18    def getMin(self):
19        return self.m[-1]
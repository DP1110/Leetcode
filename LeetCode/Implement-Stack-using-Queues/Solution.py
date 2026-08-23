1from collections import deque
2
3class MyStack(object):
4    def __init__(self):
5        self.q = deque()
6
7    def push(self, x):
8        self.q.append(x)
9        for _ in range(len(self.q) - 1):
10            self.q.append(self.q.popleft())
11
12    def pop(self):
13        return self.q.popleft()
14
15    def top(self):
16        return self.q[0]
17
18    def empty(self):
19        return len(self.q) == 0
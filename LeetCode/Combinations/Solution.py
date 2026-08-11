1class Solution(object):
2    def combine(self, n, k):
3        res = []
4        path = []
5
6        def backtrack(start):
7            if len(path) == k:
8                res.append(path[:])
9                return
10            for i in range(start, n - (k - len(path)) + 2):
11                path.append(i)
12                backtrack(i + 1)
13                path.pop()
14
15        backtrack(1)
16        return res
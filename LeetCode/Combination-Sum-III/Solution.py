1class Solution(object):
2    def combinationSum3(self, k, n):
3        res = []
4        path = []
5
6        def backtrack(start, remain, count):
7            if count == k:
8                if remain == 0:
9                    res.append(path[:])
10                return
11            for i in range(start, 10):
12                if i > remain:
13                    break
14                path.append(i)
15                backtrack(i + 1, remain - i, count + 1)
16                path.pop()
17
18        backtrack(1, n, 0)
19        return res
1class Solution(object):
2    def countSmaller(self, nums):
3        n = len(nums)
4        sorted_vals = sorted(set(nums))
5        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
6        m = len(sorted_vals)
7        tree = [0] * (m + 1)
8
9        def update(i):
10            while i <= m:
11                tree[i] += 1
12                i += i & (-i)
13
14        def query(i):
15            s = 0
16            while i > 0:
17                s += tree[i]
18                i -= i & (-i)
19            return s
20
21        res = [0] * n
22        for i in range(n - 1, -1, -1):
23            r = rank[nums[i]]
24            res[i] = query(r - 1)
25            update(r)
26        return res
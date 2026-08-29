class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        sorted_vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
        m = len(sorted_vals)
        tree = [0] * (m + 1)

        def update(i):
            while i <= m:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        res = [0] * n
        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            res[i] = query(r - 1)
            update(r)
        return res
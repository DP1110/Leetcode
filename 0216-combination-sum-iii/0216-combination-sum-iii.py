class Solution(object):
    def combinationSum3(self, k, n):
        res = []
        path = []

        def backtrack(start, remain, count):
            if count == k:
                if remain == 0:
                    res.append(path[:])
                return
            for i in range(start, 10):
                if i > remain:
                    break
                path.append(i)
                backtrack(i + 1, remain - i, count + 1)
                path.pop()

        backtrack(1, n, 0)
        return res
class Solution:
    def totalNQueens(self, n):
        cols, d1, d2 = set(), set(), set()
        cnt = [0]
        def bt(r):
            if r == n:
                cnt[0] += 1
                return
            for c in range(n):
                if c in cols or (r-c) in d1 or (r+c) in d2:
                    continue
                cols.add(c); d1.add(r-c); d2.add(r+c)
                bt(r+1)
                cols.remove(c); d1.remove(r-c); d2.remove(r+c)
        bt(0)
        return cnt[0]
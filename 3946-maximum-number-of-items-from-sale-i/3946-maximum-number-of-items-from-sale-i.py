class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        pmin = min(p for f, p in items)

        val = [0] * n
        for i in range(n):
            fi = items[i][0]
            c = 1
            for j in range(n):
                if j != i and items[j][0] % fi == 0:
                    c += 1
            val[i] = c

        dp = [0] * (budget + 1)
        for i in range(n):
            p = items[i][1]
            v = val[i]
            for b in range(budget, p - 1, -1):
                t = dp[b - p] + v
                if t > dp[b]:
                    dp[b] = t

        best = 0
        for b in range(budget + 1):
            t = dp[b] + (budget - b) // pmin
            if t > best:
                best = t
        return best
class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = 10 ** 9

        divs = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divs[L].append(d)

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divs[L]:
                    c = 0
                    m = L // d
                    for g in range(d):
                        a = i + g
                        b = i + g + (m - 1) * d
                        while a < b:
                            if s[a] != s[b]:
                                c += 1
                            a += d
                            b -= d
                    if c < best:
                        best = c
                cost[i][j] = best

        prev = [INF] * (n + 1)
        prev[0] = 0
        for p in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                for j in range(i - 1):
                    if prev[j] < INF:
                        v = prev[j] + cost[j][i - 1]
                        if v < cur[i]:
                            cur[i] = v
            prev = cur
        return prev[n]
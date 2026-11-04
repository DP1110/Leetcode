import heapq

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        lo = []          # max-heap (store negatives)
        hi = []          # min-heap
        delayed = {}
        # st = [sum_lo, sum_hi, size_lo, size_hi]
        st = [0, 0, 0, 0]

        def prune(h, neg):
            while h:
                v = -h[0] if neg else h[0]
                if delayed.get(v, 0) > 0:
                    delayed[v] -= 1
                    heapq.heappop(h)
                else:
                    break

        def balance():
            if st[2] > st[3] + 1:
                v = -heapq.heappop(lo)
                heapq.heappush(hi, v)
                st[0] -= v
                st[1] += v
                st[2] -= 1
                st[3] += 1
                prune(lo, True)
            elif st[2] < st[3]:
                v = heapq.heappop(hi)
                heapq.heappush(lo, -v)
                st[1] -= v
                st[0] += v
                st[3] -= 1
                st[2] += 1
                prune(hi, False)

        def add(v):
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v)
                st[0] += v
                st[2] += 1
            else:
                heapq.heappush(hi, v)
                st[1] += v
                st[3] += 1
            balance()

        def remove(v):
            delayed[v] = delayed.get(v, 0) + 1
            if v <= -lo[0]:
                st[0] -= v
                st[2] -= 1
                if v == -lo[0]:
                    prune(lo, True)
            else:
                st[1] -= v
                st[3] -= 1
                if hi and v == hi[0]:
                    prune(hi, False)
            balance()

        cost = [0] * (n - x + 1)
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                cost[i - x + 1] = (med * st[2] - st[0]) + (st[1] - med * st[3])

        INF = 10 ** 18
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    c = prev[i - x] + cost[i - x]
                    if c < best:
                        best = c
                cur[i] = best
            prev = cur
        return prev[n]
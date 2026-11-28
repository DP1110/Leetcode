class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            for m in range(f, n + 1, f):
                mult[f] += cnt[m]

        pm = min(p for _, p in items)
        rem, t = budget, 0
        for f, p in sorted(items, key=lambda x: x[1]):
            if p >= 2 * pm:
                break
            d = mult[f] - 1
            k = min(d, rem // p)
            t += k
            rem -= k * p
            if k < d:
                break
        return 2 * t + rem // pm
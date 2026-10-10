class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        k = k1 + k2
        n = len(diffs)
        if sum(diffs) <= k:
            return 0

        diffs.append(0)
        i = 0
        # flatten top i+1 values down to diffs[i+1] level while budget allows
        while i < n:
            cnt = i + 1
            cost = cnt * (diffs[i] - diffs[i + 1])
            if cost <= k:
                k -= cost
                i += 1
            else:
                break

        cnt = i + 1 if i < n else n
        level = diffs[i] - k // cnt
        extra = k % cnt
        # `extra` of the top cnt elements sit at level-1, the rest at level
        total = extra * (level - 1) ** 2 + (cnt - extra) * level ** 2
        for j in range(cnt, n):
            total += diffs[j] ** 2
        return total
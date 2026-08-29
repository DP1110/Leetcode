class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def max_subseq(nums, length):
            stack = []
            drop = len(nums) - length
            for x in nums:
                while stack and drop > 0 and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:length]

        def merge(a, b):
            res = []
            i = j = 0
            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res

        m, n = len(nums1), len(nums2)
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            a = max_subseq(nums1, i)
            b = max_subseq(nums2, k - i)
            cand = merge(a, b)
            if cand > best:
                best = cand
        return best
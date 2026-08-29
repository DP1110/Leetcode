1class Solution(object):
2    def maxNumber(self, nums1, nums2, k):
3        def max_subseq(nums, length):
4            stack = []
5            drop = len(nums) - length
6            for x in nums:
7                while stack and drop > 0 and stack[-1] < x:
8                    stack.pop()
9                    drop -= 1
10                stack.append(x)
11            return stack[:length]
12
13        def merge(a, b):
14            res = []
15            i = j = 0
16            while i < len(a) or j < len(b):
17                if a[i:] > b[j:]:
18                    res.append(a[i])
19                    i += 1
20                else:
21                    res.append(b[j])
22                    j += 1
23            return res
24
25        m, n = len(nums1), len(nums2)
26        best = []
27        for i in range(max(0, k - n), min(k, m) + 1):
28            a = max_subseq(nums1, i)
29            b = max_subseq(nums2, k - i)
30            cand = merge(a, b)
31            if cand > best:
32                best = cand
33        return best
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        cand1 = cand2 = None
8        cnt1 = cnt2 = 0
9        for x in nums:
10            if cand1 is not None and x == cand1:
11                cnt1 += 1
12            elif cand2 is not None and x == cand2:
13                cnt2 += 1
14            elif cnt1 == 0:
15                cand1 = x
16                cnt1 = 1
17            elif cnt2 == 0:
18                cand2 = x
19                cnt2 = 1
20            else:
21                cnt1 -= 1
22                cnt2 -= 1
23        cnt1 = cnt2 = 0
24        for x in nums:
25            if x == cand1:
26                cnt1 += 1
27            elif x == cand2:
28                cnt2 += 1
29        n = len(nums)
30        res = []
31        if cnt1 > n//3:
32            res.append(cand1)
33        if cnt2 > n//3:
34            res.append(cand2)
35        return res
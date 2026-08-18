1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        lo, hi = 0, len(numbers) - 1
9
10        while lo < hi:
11            s = numbers[lo] + numbers[hi]
12            if s == target:
13                return [lo + 1, hi + 1]
14            elif s < target:
15                lo += 1
16            else:
17                hi -= 1
18
19        return []
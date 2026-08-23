1class Solution(object):
2    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
3        if valueDiff < 0:
4            return False
5        buckets = {}
6        w = valueDiff + 1
7
8        for i, n in enumerate(nums):
9            bid = n // w
10            if bid in buckets:
11                return True
12            if bid - 1 in buckets and abs(buckets[bid-1] - n) <= valueDiff:
13                return True
14            if bid + 1 in buckets and abs(buckets[bid+1] - n) <= valueDiff:
15                return True
16            buckets[bid] = n
17            if i >= indexDiff:
18                del buckets[nums[i - indexDiff] // w]
19
20        return False
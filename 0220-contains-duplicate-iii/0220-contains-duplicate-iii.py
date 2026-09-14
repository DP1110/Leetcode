class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        buckets = {}
        w = valueDiff + 1

        for i, n in enumerate(nums):
            bid = n // w
            if bid in buckets:
                return True
            if bid - 1 in buckets and abs(buckets[bid-1] - n) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(buckets[bid+1] - n) <= valueDiff:
                return True
            buckets[bid] = n
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]

        return False
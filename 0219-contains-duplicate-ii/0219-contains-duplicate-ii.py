class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        for i, n in enumerate(nums):
            if n in last_seen and i - last_seen[n] <= k:
                return True
            last_seen[n] = i
        return False
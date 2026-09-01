from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
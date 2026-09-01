from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        c = Counter(nums1) & Counter(nums2)
        return list(c.elements())

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
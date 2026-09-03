class Solution(object):
    def uniformArray(self, nums1):
        odds = [x for x in nums1 if x % 2 == 1]
        evens = [x for x in nums1 if x % 2 == 0]

        if len(odds) == 0:
            return True

        if len(evens) == 0:
            return True
        if min(odds) < min(evens):
            return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
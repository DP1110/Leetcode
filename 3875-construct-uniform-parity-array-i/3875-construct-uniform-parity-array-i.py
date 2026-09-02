class Solution(object):
      def uniformArray(self, nums1):
        n = len(nums1)
        odd = sum(x % 2 for x in nums1)
        even = n - odd

        def feasible(p):
            for x in nums1:
                a = x % 2
                if a == p:
                    continue
                # need some other element with parity 1 (odd), excluding self
                need_odd = 1
                avail_odd = odd - (1 if a == 1 else 0)
                if avail_odd < need_odd:
                    return False
            return True

        return feasible(0) or feasible(1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
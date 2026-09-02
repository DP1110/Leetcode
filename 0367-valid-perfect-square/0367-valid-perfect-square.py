class Solution(object):
    def isPerfectSquare(self, num):
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution(object):
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
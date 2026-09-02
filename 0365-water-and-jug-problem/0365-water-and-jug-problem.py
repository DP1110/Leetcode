from fractions import gcd

class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False
        if target == 0:
            return True
        return target % gcd(x, y) == 0
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
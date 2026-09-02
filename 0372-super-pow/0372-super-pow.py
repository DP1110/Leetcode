class Solution(object):
    def superPow(self, a, b):
        MOD = 1337
        result = 1
        a %= MOD
        for digit in b:
            result = pow(result, 10, MOD) * pow(a, digit, MOD) % MOD
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
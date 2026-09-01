class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        chars = list(s)
        l, r = 0, len(chars) - 1
        while l < r:
            if chars[l] not in vowels:
                l += 1
            elif chars[r] not in vowels:
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        return ''.join(chars)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
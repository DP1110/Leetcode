class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Build reversed_half from the last half of digits
        # Stop when reversed_half >= x (we've processed half or more)
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Even length: x == reversed_half
        # Odd length: x == reversed_half // 10 (middle digit ignored)
        return x == reversed_half or x == reversed_half // 10
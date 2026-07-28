1class Solution(object):
2    def isPalindrome(self, x):
3        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
4        if x < 0 or (x % 10 == 0 and x != 0):
5            return False
6        
7        reversed_half = 0
8        
9        # Build reversed_half from the last half of digits
10        # Stop when reversed_half >= x (we've processed half or more)
11        while x > reversed_half:
12            reversed_half = reversed_half * 10 + x % 10
13            x //= 10
14        
15        # Even length: x == reversed_half
16        # Odd length: x == reversed_half // 10 (middle digit ignored)
17        return x == reversed_half or x == reversed_half // 10
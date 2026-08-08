class Solution:
    def getPermutation(self, n, k):
        # Precompute factorials: factorial[i] = i!
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        # Available numbers to pick from
        numbers = list(range(1, n + 1))
        
        # Convert k to 0-indexed
        k -= 1
        
        result = []
        
        # Build the permutation digit by digit
        for i in range(n, 0, -1):
            fact = factorial[i - 1]          # (i-1)!
            index = k // fact                # Which number to pick
            k %= fact                        # Update k for next iteration
            
            result.append(str(numbers[index]))
            numbers.pop(index)               # Remove used number
        
        return "".join(result)
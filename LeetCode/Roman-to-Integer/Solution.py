1class Solution(object):
2    def romanToInt(self, s):
3        # Map each Roman symbol to its value
4        values = {
5            'I': 1,
6            'V': 5,
7            'X': 10,
8            'L': 50,
9            'C': 100,
10            'D': 500,
11            'M': 1000
12        }
13        
14        total = 0
15        n = len(s)
16        
17        for i in range(n):
18            current = values[s[i]]
19            # If next value exists and is larger, this is a subtractive pair
20            if i + 1 < n and current < values[s[i + 1]]:
21                total -= current
22            else:
23                total += current
24        
25        return total
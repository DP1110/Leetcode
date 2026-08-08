1class Solution:
2    def isNumber(self, s):
3        state = 0  # 0 = start
4        
5        for c in s:
6            if state == 0:      # start
7                if c in '+-':   state = 1
8                elif c.isdigit(): state = 2
9                elif c == '.':  state = 3
10                else: return False
11            elif state == 1:    # sign before number
12                if c.isdigit(): state = 2
13                elif c == '.':  state = 3
14                else: return False
15            elif state == 2:    # integer digits
16                if c.isdigit(): state = 2
17                elif c == '.':  state = 4
18                elif c in 'eE': state = 6
19                else: return False
20            elif state == 3:    # dot with NO leading digits (e.g., ".")
21                if c.isdigit(): state = 5
22                else: return False
23            elif state == 4:    # dot WITH leading digits (e.g., "5.")
24                if c.isdigit(): state = 5
25                elif c in 'eE': state = 6
26                else: return False
27            elif state == 5:    # fractional digits
28                if c.isdigit(): state = 5
29                elif c in 'eE': state = 6
30                else: return False
31            elif state == 6:    # exponent e/E
32                if c in '+-':   state = 7
33                elif c.isdigit(): state = 8
34                else: return False
35            elif state == 7:    # sign after exponent
36                if c.isdigit(): state = 8
37                else: return False
38            elif state == 8:    # exponent digits
39                if c.isdigit(): state = 8
40                else: return False
41        
42        # Valid ending states: integer, dot-with-digits, fraction, exponent-digits
43        return state in (2, 4, 5, 8)
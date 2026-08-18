1class Solution(object):
2    def fractionToDecimal(self, numerator, denominator):
3        """
4        :type numerator: int
5        :type denominator: int
6        :rtype: str
7        """
8        if numerator == 0:
9            return "0"
10
11        result = []
12
13        # sign
14        neg = (numerator < 0) != (denominator < 0)
15        if neg:
16            result.append('-')
17
18        num = abs(numerator)
19        den = abs(denominator)
20
21        # integer part
22        int_part = num // den
23        result.append(str(int_part))
24
25        rem = num % den
26        if rem == 0:
27            return ''.join(result)
28
29        result.append('.')
30
31        # fractional part, track remainder positions for cycle
32        seen = {}  # remainder -> index in frac list
33        frac = []
34
35        while rem != 0:
36            if rem in seen:
37                idx = seen[rem]
38                frac.insert(idx, '(')
39                frac.append(')')
40                break
41            seen[rem] = len(frac)
42            rem *= 10
43            frac.append(str(rem // den))
44            rem = rem % den
45
46        result.append(''.join(frac))
47
48        return ''.join(result)
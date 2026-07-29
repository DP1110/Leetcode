1class Solution(object):
2    def intToRoman(self, num):
3        # Values and symbols in descending order, including subtractive forms
4        val_sym = [
5            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
6            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
7            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
8        ]
9        
10        result = []
11        for value, symbol in val_sym:
12            # Append symbol while we can subtract this value
13            while num >= value:
14                result.append(symbol)
15                num -= value
16        
17        return "".join(result)
class Solution:
    def isNumber(self, s):
        state = 0  # 0 = start
        
        for c in s:
            if state == 0:      # start
                if c in '+-':   state = 1
                elif c.isdigit(): state = 2
                elif c == '.':  state = 3
                else: return False
            elif state == 1:    # sign before number
                if c.isdigit(): state = 2
                elif c == '.':  state = 3
                else: return False
            elif state == 2:    # integer digits
                if c.isdigit(): state = 2
                elif c == '.':  state = 4
                elif c in 'eE': state = 6
                else: return False
            elif state == 3:    # dot with NO leading digits (e.g., ".")
                if c.isdigit(): state = 5
                else: return False
            elif state == 4:    # dot WITH leading digits (e.g., "5.")
                if c.isdigit(): state = 5
                elif c in 'eE': state = 6
                else: return False
            elif state == 5:    # fractional digits
                if c.isdigit(): state = 5
                elif c in 'eE': state = 6
                else: return False
            elif state == 6:    # exponent e/E
                if c in '+-':   state = 7
                elif c.isdigit(): state = 8
                else: return False
            elif state == 7:    # sign after exponent
                if c.isdigit(): state = 8
                else: return False
            elif state == 8:    # exponent digits
                if c.isdigit(): state = 8
                else: return False
        
        # Valid ending states: integer, dot-with-digits, fraction, exponent-digits
        return state in (2, 4, 5, 8)
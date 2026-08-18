class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        result = []

        # sign
        neg = (numerator < 0) != (denominator < 0)
        if neg:
            result.append('-')

        num = abs(numerator)
        den = abs(denominator)

        # integer part
        int_part = num // den
        result.append(str(int_part))

        rem = num % den
        if rem == 0:
            return ''.join(result)

        result.append('.')

        # fractional part, track remainder positions for cycle
        seen = {}  # remainder -> index in frac list
        frac = []

        while rem != 0:
            if rem in seen:
                idx = seen[rem]
                frac.insert(idx, '(')
                frac.append(')')
                break
            seen[rem] = len(frac)
            rem *= 10
            frac.append(str(rem // den))
            rem = rem % den

        result.append(''.join(frac))

        return ''.join(result)
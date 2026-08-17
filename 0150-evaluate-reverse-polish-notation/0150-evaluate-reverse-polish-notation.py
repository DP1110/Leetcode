class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = set(['+', '-', '*', '/'])

        for tok in tokens:
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                if tok == '+':
                    res = a + b
                elif tok == '-':
                    res = a - b
                elif tok == '*':
                    res = a * b
                else:
                    # truncate toward zero, not floor
                    res = int(a * 1.0 / b) if (a < 0) != (b < 0) else a // b
                stack.append(res)
            else:
                stack.append(int(tok))

        return stack.pop()
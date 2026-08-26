class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                   "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                   "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [below20[n]]
            elif n < 100:
                return [tens[n // 10]] + helper(n % 10)
            else:
                return [below20[n // 100], "Hundred"] + helper(n % 100)

        res = []
        i = 0
        while num > 0:
            if num % 1000 != 0:
                chunk = helper(num % 1000)
                if thousands[i]:
                    chunk.append(thousands[i])
                res = chunk + res
            num //= 1000
            i += 1

        return " ".join(res)
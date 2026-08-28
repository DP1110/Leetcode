1class Solution(object):
2    def maxProfit(self, prices):
3        if not prices:
4            return 0
5        hold = -prices[0]
6        sold = 0
7        rest = 0
8        for p in prices[1:]:
9            prev_sold = sold
10            sold = hold + p
11            hold = max(hold, rest - p)
12            rest = max(rest, prev_sold)
13        return max(sold, rest)
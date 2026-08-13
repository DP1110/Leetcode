1class Solution(object):
2    def maxProfit(self, prices):
3        min_price = float('inf')
4        max_profit = 0
5        for p in prices:
6            min_price = min(min_price, p)
7            max_profit = max(max_profit, p - min_price)
8        return max_profit
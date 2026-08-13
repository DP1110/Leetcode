1class Solution(object):
2    def maxProfit(self, prices):
3        buy1 = buy2 = float('-inf')
4        sell1 = sell2 = 0
5        for p in prices:
6            buy1 = max(buy1, -p)
7            sell1 = max(sell1, buy1 + p)
8            buy2 = max(buy2, sell1 - p)
9            sell2 = max(sell2, buy2 + p)
10        return sell2
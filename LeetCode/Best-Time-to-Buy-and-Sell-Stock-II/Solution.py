1class Solution(object):
2    def maxProfit(self, prices):
3        profit = 0
4        for i in range(1, len(prices)):
5            if prices[i] > prices[i-1]:
6                profit += prices[i] - prices[i-1]
7        return profit
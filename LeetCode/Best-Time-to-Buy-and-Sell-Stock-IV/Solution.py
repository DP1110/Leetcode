1class Solution(object):
2    def maxProfit(self, k, prices):
3        n = len(prices)
4        if n == 0 or k == 0:
5            return 0
6        if k >= n // 2:
7            profit = 0
8            for i in range(1, n):
9                if prices[i] > prices[i-1]:
10                    profit += prices[i] - prices[i-1]
11            return profit
12
13        buy = [-float('inf')] * (k + 1)
14        sell = [0] * (k + 1)
15        for p in prices:
16            for j in range(1, k + 1):
17                buy[j] = max(buy[j], sell[j-1] - p)
18                sell[j] = max(sell[j], buy[j] + p)
19        return sell[k]
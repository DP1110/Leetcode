class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j-1] - p)
                sell[j] = max(sell[j], buy[j] + p)
        return sell[k]
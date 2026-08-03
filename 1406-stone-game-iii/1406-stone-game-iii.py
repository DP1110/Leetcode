class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        # dp1, dp2, dp3 store dp[i+1], dp[i+2], dp[i+3]
        # dp[i] = max score difference (current_player - opponent) starting from i
        dp1 = dp2 = dp3 = 0
        
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp1
            
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - dp2
            else:
                take2 = float('-inf')
            
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp3
            else:
                take3 = float('-inf')
            
            curr = max(take1, take2, take3)
            dp1, dp2, dp3 = curr, dp1, dp2
        
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"
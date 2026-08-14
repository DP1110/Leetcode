1class Solution(object):
2    def partition(self, s):
3        n = len(s)
4        
5        # dp[i][j] = True if s[i:j+1] is a palindrome
6        dp = [[False] * n for _ in range(n)]
7        for i in range(n - 1, -1, -1):
8            for j in range(i, n):
9                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
10                    dp[i][j] = True
11        
12        result = []
13        
14        def backtrack(start, path):
15            if start == n:
16                result.append(path[:])
17                return
18            
19            for end in range(start, n):
20                if dp[start][end]:
21                    path.append(s[start:end + 1])
22                    backtrack(end + 1, path)
23                    path.pop()
24        
25        backtrack(0, [])
26        return result
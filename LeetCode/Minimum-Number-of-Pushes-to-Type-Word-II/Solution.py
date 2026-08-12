1class Solution(object):
2    def minimumPushes(self, word):
3        # Use array instead of Counter - much faster
4        count = [0] * 26
5        for ch in word:
6            count[ord(ch) - 97] += 1  # 97 is ord('a')
7        
8        # Sort descending
9        count.sort(reverse=True)
10        
11        total = 0
12        for i in range(26):
13            if count[i] == 0:
14                break
15            total += count[i] * ((i // 8) + 1)
16        
17        return total
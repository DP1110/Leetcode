1class Solution:
2    def countAndSay(self, n):
3        s = "1"
4        
5        for _ in range(n - 1):
6            next_s = []
7            i = 0
8            
9            while i < len(s):
10                count = 1
11                # Count consecutive identical digits
12                while i + 1 < len(s) and s[i] == s[i + 1]:
13                    count += 1
14                    i += 1
15                
16                next_s.append(str(count))
17                next_s.append(s[i])
18                i += 1
19            
20            s = "".join(next_s)
21        
22        return s
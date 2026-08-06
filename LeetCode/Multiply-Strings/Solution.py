1class Solution:
2    def multiply(self, num1, num2):
3        if num1 == "0" or num2 == "0":
4            return "0"
5        
6        m, n = len(num1), len(num2)
7        result = [0] * (m + n)
8        
9        for i in range(m - 1, -1, -1):
10            for j in range(n - 1, -1, -1):
11                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
12                p1, p2 = i + j, i + j + 1
13                total = mul + result[p2]
14                
15                result[p2] = total % 10
16                result[p1] += total // 10
17        
18        # Skip leading zeros
19        i = 0
20        while i < len(result) and result[i] == 0:
21            i += 1
22        
23        return "".join(str(d) for d in result[i:])
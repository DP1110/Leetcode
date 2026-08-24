1class Solution(object):
2    def countDigitOne(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        count = 0
8        place = 1
9        while place <= n:
10            high = n // (place*10)
11            cur = (n // place) % 10
12            low = n % place
13            if cur == 0:
14                count += high*place
15            elif cur == 1:
16                count += high*place + low + 1
17            else:
18                count += (high+1)*place
19            place *= 10
20        return count
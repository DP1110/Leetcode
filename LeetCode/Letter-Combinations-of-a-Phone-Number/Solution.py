1class Solution:
2    def letterCombinations(self, digits):
3        if not digits:
4            return []
5        
6        phone = {
7            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
8            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
9        }
10        
11        result = [""]
12        for digit in digits:
13            temp = []
14            for combo in result:
15                for letter in phone[digit]:
16                    temp.append(combo + letter)
17            result = temp
18        
19        return result
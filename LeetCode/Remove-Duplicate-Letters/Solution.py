1class Solution(object):
2    def removeDuplicateLetters(self, s):
3        last_occurrence = {c: i for i, c in enumerate(s)}
4        stack = []
5        in_stack = set()
6
7        for i, c in enumerate(s):
8            if c in in_stack:
9                continue
10            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
11                in_stack.remove(stack.pop())
12            stack.append(c)
13            in_stack.add(c)
14
15        return ''.join(stack)
1class Solution(object):
2    def ladderLength(self, beginWord, endWord, wordList):
3        wordSet = set(wordList)
4        if endWord not in wordSet:
5            return 0
6        
7        from collections import deque
8        queue = deque([(beginWord, 1)])
9        visited = set([beginWord])
10        
11        while queue:
12            word, steps = queue.popleft()
13            if word == endWord:
14                return steps
15            
16            for i in range(len(word)):
17                for c in 'abcdefghijklmnopqrstuvwxyz':
18                    next_word = word[:i] + c + word[i+1:]
19                    if next_word in wordSet and next_word not in visited:
20                        visited.add(next_word)
21                        queue.append((next_word, steps + 1))
22        
23        return 0
1class Solution(object):
2    def findLadders(self, beginWord, endWord, wordList):
3        wordSet = set(wordList)
4        if endWord not in wordSet:
5            return []
6        
7        # BFS to build shortest path graph
8        from collections import deque, defaultdict
9        queue = deque([beginWord])
10        dist = {beginWord: 0}
11        parents = defaultdict(list)
12        found = False
13        L = len(beginWord)
14        
15        while queue and not found:
16            size = len(queue)
17            # Track words visited at this level to avoid duplicates in queue
18            # Actually, we can process level by level
19            for _ in range(size):
20                word = queue.popleft()
21                for i in range(L):
22                    for c in 'abcdefghijklmnopqrstuvwxyz':
23                        next_word = word[:i] + c + word[i+1:]
24                        if next_word not in wordSet:
25                            continue
26                        if next_word not in dist:
27                            dist[next_word] = dist[word] + 1
28                            queue.append(next_word)
29                            parents[next_word].append(word)
30                        elif dist[next_word] == dist[word] + 1:
31                            parents[next_word].append(word)
32                        if next_word == endWord:
33                            found = True
34            # Optimization: if found, we can stop BFS after this level
35            # But we need to finish processing this level to get all parents
36            # The 'found' flag handles this: we process the full level where endWord is found
37        
38        if endWord not in dist:
39            return []
40        
41        # DFS from endWord to beginWord
42        result = []
43        path = [endWord]
44        
45        def dfs(word):
46            if word == beginWord:
47                result.append(path[::-1])
48                return
49            for parent in parents[word]:
50                path.append(parent)
51                dfs(parent)
52                path.pop()
53        
54        dfs(endWord)
55        return result
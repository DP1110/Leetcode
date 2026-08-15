class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # BFS to build shortest path graph
        from collections import deque, defaultdict
        queue = deque([beginWord])
        dist = {beginWord: 0}
        parents = defaultdict(list)
        found = False
        L = len(beginWord)
        
        while queue and not found:
            size = len(queue)
            # Track words visited at this level to avoid duplicates in queue
            # Actually, we can process level by level
            for _ in range(size):
                word = queue.popleft()
                for i in range(L):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word not in wordSet:
                            continue
                        if next_word not in dist:
                            dist[next_word] = dist[word] + 1
                            queue.append(next_word)
                            parents[next_word].append(word)
                        elif dist[next_word] == dist[word] + 1:
                            parents[next_word].append(word)
                        if next_word == endWord:
                            found = True
            # Optimization: if found, we can stop BFS after this level
            # But we need to finish processing this level to get all parents
            # The 'found' flag handles this: we process the full level where endWord is found
        
        if endWord not in dist:
            return []
        
        # DFS from endWord to beginWord
        result = []
        path = [endWord]
        
        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()
        
        dfs(endWord)
        return result
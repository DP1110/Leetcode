1class WordDictionary(object):
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
5
6    def addWord(self, word):
7        node = self
8        for ch in word:
9            if ch not in node.children:
10                node.children[ch] = WordDictionary()
11            node = node.children[ch]
12        node.is_end = True
13
14    def search(self, word):
15        node = self
16        return self._dfs(node, word, 0)
17
18    def _dfs(self, node, word, i):
19        if i == len(word):
20            return node.is_end
21        ch = word[i]
22        if ch == '.':
23            for child in node.children.values():
24                if self._dfs(child, word, i + 1):
25                    return True
26            return False
27        else:
28            if ch not in node.children:
29                return False
30            return self._dfs(node.children[ch], word, i + 1)
1class Trie(object):
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
5
6    def insert(self, word):
7        node = self
8        for ch in word:
9            if ch not in node.children:
10                node.children[ch] = Trie()
11            node = node.children[ch]
12        node.is_end = True
13
14    def search(self, word):
15        node = self._find(word)
16        return node is not None and node.is_end
17
18    def startsWith(self, prefix):
19        return self._find(prefix) is not None
20
21    def _find(self, s):
22        node = self
23        for ch in s:
24            if ch not in node.children:
25                return None
26            node = node.children[ch]
27        return node
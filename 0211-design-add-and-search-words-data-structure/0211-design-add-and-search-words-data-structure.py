class WordDictionary(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self
        return self._dfs(node, word, 0)

    def _dfs(self, node, word, i):
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == '.':
            for child in node.children.values():
                if self._dfs(child, word, i + 1):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(node.children[ch], word, i + 1)
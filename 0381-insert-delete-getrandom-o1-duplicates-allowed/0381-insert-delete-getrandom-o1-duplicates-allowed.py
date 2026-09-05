import random
from collections import defaultdict

class RandomizedCollection(object):
    def __init__(self):
        self.arr = []
        self.idx = defaultdict(set)

    def insert(self, val):
        present = val in self.idx and len(self.idx[val]) > 0
        self.idx[val].add(len(self.arr))
        self.arr.append(val)
        return not present

    def remove(self, val):
        if not self.idx.get(val):
            return False
        i = self.idx[val].pop()
        last_idx = len(self.arr) - 1
        last_val = self.arr[last_idx]
        self.arr[i] = last_val
        if i != last_idx:
            self.idx[last_val].discard(last_idx)
            self.idx[last_val].add(i)
        self.arr.pop()
        return True

    def getRandom(self):
        return random.choice(self.arr)
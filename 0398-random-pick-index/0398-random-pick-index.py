import random
from collections import defaultdict

class Solution(object):
    def __init__(self, nums):
        self.idx = defaultdict(list)
        for i, x in enumerate(nums):
            self.idx[x].append(i)

    def pick(self, target):
        lst = self.idx[target]
        return lst[random.randrange(len(lst))]
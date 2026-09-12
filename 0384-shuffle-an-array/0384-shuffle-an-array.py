import random

class Solution(object):
    def __init__(self, nums):
        self.original = list(nums)
        self.arr = list(nums)

    def reset(self):
        self.arr = list(self.original)
        return self.arr

    def shuffle(self):
        for i in range(len(self.arr) - 1, 0, -1):
            j = random.randint(0, i)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
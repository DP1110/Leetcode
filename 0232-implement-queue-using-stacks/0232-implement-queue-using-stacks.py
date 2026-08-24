class MyQueue(object):

    def __init__(self):
        self.instk = []
        self.outstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.instk.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self._transfer()
        return self.outstk.pop()

    def peek(self):
        """
        :rtype: int
        """
        self._transfer()
        return self.outstk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.instk and not self.outstk

    def _transfer(self):
        if not self.outstk:
            while self.instk:
                self.outstk.append(self.instk.pop())
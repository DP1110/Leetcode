class Solution(object):
    def canAliceWin(self, n):
      
        take = 10
        alice = True
        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice = not alice
        # alice = True means Alice's turn and she can't move -> she loses
        return not alice
        
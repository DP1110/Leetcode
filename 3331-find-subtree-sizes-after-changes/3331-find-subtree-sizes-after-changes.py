class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        ch = [[] for _ in range(n)]
        for i in range(1, n):
            ch[parent[i]].append(i)

        last = [-1] * 26
        newp = parent[:]
        saved = [-1] * n
        order = []
        stack = [(0, 0)]
        while stack:
            x, st = stack.pop()
            c = ord(s[x]) - 97
            if st == 0:
                order.append(x)
                if last[c] != -1:
                    newp[x] = last[c]
                saved[x] = last[c]
                last[c] = x
                stack.append((x, 1))
                for y in ch[x]:
                    stack.append((y, 0))
            else:
                last[c] = saved[x]

        size = [1] * n
        for x in reversed(order):
            if x != 0:
                size[newp[x]] += size[x]
        return size
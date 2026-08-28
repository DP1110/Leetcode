1class Solution(object):
2    def findMinHeightTrees(self, n, edges):
3        if n == 1:
4            return [0]
5        graph = [set() for _ in range(n)]
6        for a, b in edges:
7            graph[a].add(b)
8            graph[b].add(a)
9        leaves = [i for i in range(n) if len(graph[i]) == 1]
10        remaining = n
11        while remaining > 2:
12            remaining -= len(leaves)
13            new_leaves = []
14            for leaf in leaves:
15                nb = graph[leaf].pop()
16                graph[nb].remove(leaf)
17                if len(graph[nb]) == 1:
18                    new_leaves.append(nb)
19            leaves = new_leaves
20        return leaves
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nb = graph[leaf].pop()
                graph[nb].remove(leaf)
                if len(graph[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves
        return leaves
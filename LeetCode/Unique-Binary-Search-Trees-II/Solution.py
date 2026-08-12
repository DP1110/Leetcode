1class Solution(object):
2    def generateTrees(self, n):
3        if n == 0:
4            return []
5
6        def build(lo, hi):
7            if lo > hi:
8                return [None]
9
10            trees = []
11            for root_val in range(lo, hi + 1):
12                left_subtrees = build(lo, root_val - 1)
13                right_subtrees = build(root_val + 1, hi)
14
15                for l in left_subtrees:
16                    for r in right_subtrees:
17                        node = TreeNode(root_val)
18                        node.left = l
19                        node.right = r
20                        trees.append(node)
21            return trees
22
23        return build(1, n)
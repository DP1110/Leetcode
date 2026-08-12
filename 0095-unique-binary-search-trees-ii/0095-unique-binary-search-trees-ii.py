class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []

        def build(lo, hi):
            if lo > hi:
                return [None]

            trees = []
            for root_val in range(lo, hi + 1):
                left_subtrees = build(lo, root_val - 1)
                right_subtrees = build(root_val + 1, hi)

                for l in left_subtrees:
                    for r in right_subtrees:
                        node = TreeNode(root_val)
                        node.left = l
                        node.right = r
                        trees.append(node)
            return trees

        return build(1, n)
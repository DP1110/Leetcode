class Solution(object):
    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)
            s = l_sum + r_sum + node.val
            c = l_cnt + r_cnt + 1
            if s // c == node.val:
                self.count += 1
            return (s, c)

        dfs(root)
        return self.count
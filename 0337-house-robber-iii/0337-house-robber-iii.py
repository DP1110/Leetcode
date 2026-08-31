class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            l_rob, l_skip = dfs(node.left)
            r_rob, r_skip = dfs(node.right)
            rob_this = node.val + l_skip + r_skip
            skip_this = max(l_rob, l_skip) + max(r_rob, r_skip)
            return (rob_this, skip_this)
        return max(dfs(root))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            nxt = []
            for node in queue:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
        return res
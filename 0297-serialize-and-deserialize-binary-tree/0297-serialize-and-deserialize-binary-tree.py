class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def build():
            v = next(vals)
            if v == '#':
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node
        return build()
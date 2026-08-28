1class Codec:
2    def serialize(self, root):
3        vals = []
4        def dfs(node):
5            if not node:
6                vals.append('#')
7                return
8            vals.append(str(node.val))
9            dfs(node.left)
10            dfs(node.right)
11        dfs(root)
12        return ','.join(vals)
13
14    def deserialize(self, data):
15        vals = iter(data.split(','))
16        def build():
17            v = next(vals)
18            if v == '#':
19                return None
20            node = TreeNode(int(v))
21            node.left = build()
22            node.right = build()
23            return node
24        return build()
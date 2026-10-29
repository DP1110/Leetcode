class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        s = list(s)
        bit = lambda ch: 1 << (ord(ch) - 97)

        # preorder via stack, subtree is contiguous
        par = [0] * n
        tin = [0] * n
        order = []
        seen = [False] * n
        stack = [0]
        seen[0] = True
        while stack:
            v = stack.pop()
            tin[v] = len(order)
            order.append(v)
            for w in adj[v]:
                if not seen[w]:
                    seen[w] = True
                    par[w] = v
                    stack.append(w)

        size = [1] * n
        for v in reversed(order):
            if v != 0:
                size[par[v]] += size[v]
        tout = [tin[v] + size[v] - 1 for v in range(n)]

        # base prefix mask root->v
        base = [0] * n
        for v in order:
            base[v] = (base[par[v]] if v != 0 else 0) ^ bit(s[v])

        # binary lifting
        LOG = max(1, n.bit_length())
        up = [par[:]]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def anc(a, b):
            return tin[a] <= tin[b] <= tout[a]

        def lca(u, v):
            if anc(u, v):
                return u
            if anc(v, u):
                return v
            for k in range(LOG - 1, -1, -1):
                w = up[k][u]
                if not anc(w, v):
                    u = w
            return up[0][u]

        # BIT: range xor update, point query
        tree = [0] * (n + 2)

        def add(i, d):
            i += 1
            while i <= n + 1:
                tree[i] ^= d
                i += i & -i

        def get(i):
            i += 1
            r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r

        def P(x):
            return base[x] ^ get(tin[x])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                d = bit(s[u]) ^ bit(c)
                if d:
                    s[u] = c
                    add(tin[u], d)
                    add(tout[u] + 1, d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = P(u) ^ P(v) ^ bit(s[l])
                ans.append(m & (m - 1) == 0)
        return ans
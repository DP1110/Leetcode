class Solution(object):
    def canCross(self, stones):
        if stones[1] != 1:
            return False
        stone_set = set(stones)
        target = stones[-1]
        visited = set()

        def dfs(pos, k):
            if pos == target:
                return True
            if (pos, k) in visited:
                return False
            visited.add((pos, k))
            for dk in (-1, 0, 1):
                nk = k + dk
                if nk <= 0:
                    continue
                np = pos + nk
                if np in stone_set and dfs(np, nk):
                    return True
            return False

        return dfs(1, 1)
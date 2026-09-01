from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        # Coaching Analysis:
        # Your approach uses BFS with a state of (row, col, energy, mask).
        # This is conceptually correct for finding the shortest path in a state-space.
        #
        # Current Time Complexity: O(M * N * Energy * 2^L) where L is number of litters.
        # Current Space Complexity: O(M * N * Energy * 2^L) to store the best_energy map.
        #
        # Potential Issues:
        # 1. Efficiency: If Energy is large, the state space (r, c, mask) might be better 
        #    tracked by the maximum remaining energy at that state.
        # 2. State Pruning: You are using best_energy.get((r, c, mask), -1) > e.
        #    Since this is BFS, the first time you reach a state (r, c, mask) with 
        #    a certain energy, it's the minimum moves. However, reaching the same 
        #    state with MORE energy later might be beneficial.
        #
        # Optimal Approach:
        # This is a shortest path problem on a graph. Since edges have weight 1, 
        # BFS is correct, but the state must be (r, c, mask, current_energy).
        # Given the constraints of "Medium" problems, ensure L (litters) is small (usually < 15).
        
        m = len(classroom)
        n = len(classroom[0])
        litter_idx = {}
        start = None
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter_idx[(i, j)] = len(litter_idx)

        full_mask = (1 << len(litter_idx)) - 1
        if full_mask == 0:
            return 0

        sr, sc = start
        init_mask = 0
        if (sr, sc) in litter_idx:
            init_mask |= 1 << litter_idx[(sr, sc)]

        best_energy = {}
        start_key = (sr, sc, init_mask)
        best_energy[start_key] = energy
        q = deque([(sr, sc, energy, init_mask, 0)])

        while q:
            r, c, e, mask, moves = q.popleft()
            if mask == full_mask:
                return moves
            if e == 0:
                continue
            if best_energy.get((r, c, mask), -1) > e:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = energy if classroom[nr][nc] == 'R' else e - 1
                    nmask = mask
                    if (nr, nc) in litter_idx:
                        nmask |= 1 << litter_idx[(nr, nc)]
                    key = (nr, nc, nmask)
                    if ne > best_energy.get(key, -1):
                        best_energy[key] = ne
                        q.append((nr, nc, ne, nmask, moves + 1))

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
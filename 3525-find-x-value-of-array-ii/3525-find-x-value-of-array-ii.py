class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # prod[i] = product of segment i modulo k
        # count[i] = prefix counts for every residue modulo k
        prod = [1] * (2 * n)
        count = [[0] * k for _ in range(2 * n)]

        def merge(left_prod, left_count, right_prod, right_count):
            new_prod = left_prod * right_prod % k
            new_count = left_count[:]

            for residue in range(k):
                if right_count[residue]:
                    new_residue = left_prod * residue % k
                    new_count[new_residue] += right_count[residue]

            return new_prod, new_count

        # Build leaves.
        for i in range(n):
            residue = nums[i] % k
            prod[n + i] = residue
            count[n + i][residue] = 1

        # Build internal nodes.
        for i in range(n - 1, 0, -1):
            prod[i], count[i] = merge(
                prod[i << 1], count[i << 1],
                prod[i << 1 | 1], count[i << 1 | 1]
            )

        def update(index, value):
            position = index + n
            residue = value % k

            prod[position] = residue
            count[position] = [0] * k
            count[position][residue] = 1

            position //= 2
            while position:
                prod[position], count[position] = merge(
                    prod[position << 1], count[position << 1],
                    prod[position << 1 | 1], count[position << 1 | 1]
                )
                position //= 2

        def query(left, right):
            """Query the half-open interval [left, right)."""
            left_prod = 1
            left_count = [0] * k

            right_prod = 1
            right_count = [0] * k

            left += n
            right += n

            while left < right:
                if left & 1:
                    left_prod, left_count = merge(
                        left_prod, left_count,
                        prod[left], count[left]
                    )
                    left += 1

                if right & 1:
                    right -= 1
                    right_prod, right_count = merge(
                        prod[right], count[right],
                        right_prod, right_count
                    )

                left //= 2
                right //= 2

            return merge(left_prod, left_count,
                         right_prod, right_count)

        answer = []

        for index, value, start, x in queries:
            # Update persists across later queries.
            update(index, value)

            # Prefix removal is temporary.
            _, prefix_counts = query(start, n)
            answer.append(prefix_counts[x])

        return answer
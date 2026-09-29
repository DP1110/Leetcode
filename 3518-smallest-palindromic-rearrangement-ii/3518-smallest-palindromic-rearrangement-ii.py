class Solution(object):
    def smallestPalindrome(self, s, k):
        from collections import Counter
        CAP = 2 * 10 ** 6

        n = len(s)
        cnt = Counter(s)
        mid_char = None
        half_counts = {}
        for ch, c in cnt.items():
            if c % 2 == 1:
                mid_char = ch
            half_counts[ch] = c // 2

        letters = sorted(half_counts.keys())

        def count_perms(counts_dict):
            counts = [counts_dict[ch] for ch in letters]
            total = sum(counts)
            if total == 0:
                return 1
            result = 1
            remaining = total
            for c in counts:
                if c == 0:
                    continue
                r = 1
                for i in range(1, c + 1):
                    r = r * (remaining - c + i) // i
                    if r > CAP:
                        r = CAP + 1
                        break
                result *= r
                if result > CAP:
                    return CAP + 1
                remaining -= c
            return result

        total_perms = count_perms(half_counts)
        if total_perms < k:
            return ""

        half = n // 2
        result_chars = []
        remaining = dict(half_counts)

        for _ in range(half):
            for ch in letters:
                if remaining[ch] == 0:
                    continue
                remaining[ch] -= 1
                c = count_perms(remaining)
                if c >= k:
                    result_chars.append(ch)
                    break
                else:
                    k -= c
                    remaining[ch] += 1

        left = ''.join(result_chars)
        right = left[::-1]
        mid = mid_char if mid_char is not None else ""
        return left + mid + right
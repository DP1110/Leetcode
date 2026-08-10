from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)  # total char still need

        left = 0
        best_left, best_right = 0, 0  # best window bound, empty init

        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:  # valid window, shrink left
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if best_right == 0 or right - left < best_right - best_left:
                    best_left, best_right = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[best_left:best_right]
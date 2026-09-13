class Solution(object):
    def longestSubstring(self, s, k):
        def helper(s, k):
            if len(s) < k:
                return 0
            for c in set(s):
                if s.count(c) < k:
                    return max(helper(part, k) for part in s.split(c))
            return len(s)
        return helper(s, k)
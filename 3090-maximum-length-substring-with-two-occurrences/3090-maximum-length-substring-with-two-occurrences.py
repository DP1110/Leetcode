class Solution(object):
    def maximumLengthSubstring(self, s):
        count = [0] * 26
        left = 0
        max_len = 0
        base = ord('a')
        
        for right, ch in enumerate(s):
            idx = ord(ch) - base
            count[idx] += 1
            
            while count[idx] > 2:
                count[ord(s[left]) - base] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
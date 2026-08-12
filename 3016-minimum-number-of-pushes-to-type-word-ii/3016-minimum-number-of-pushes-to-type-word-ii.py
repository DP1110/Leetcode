class Solution(object):
    def minimumPushes(self, word):
        # Use array instead of Counter - much faster
        count = [0] * 26
        for ch in word:
            count[ord(ch) - 97] += 1  # 97 is ord('a')
        
        # Sort descending
        count.sort(reverse=True)
        
        total = 0
        for i in range(26):
            if count[i] == 0:
                break
            total += count[i] * ((i // 8) + 1)
        
        return total
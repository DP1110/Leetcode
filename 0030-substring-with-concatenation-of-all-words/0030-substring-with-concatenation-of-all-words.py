class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
        
        # Build frequency map of words
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        # Try every possible starting offset within a word length
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            count = 0
            
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1
                    
                    # Shrink window from left if we have too many of this word
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # Check if window contains exactly all words
                    if count == num_words:
                        result.append(left)
                else:
                    # Invalid word found, reset window
                    current_count.clear()
                    count = 0
                    left = right
        
        return result
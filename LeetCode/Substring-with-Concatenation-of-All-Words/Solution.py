1class Solution:
2    def findSubstring(self, s, words):
3        if not s or not words:
4            return []
5        
6        word_len = len(words[0])
7        num_words = len(words)
8        total_len = word_len * num_words
9        s_len = len(s)
10        
11        if s_len < total_len:
12            return []
13        
14        # Build frequency map of words
15        word_count = {}
16        for word in words:
17            word_count[word] = word_count.get(word, 0) + 1
18        
19        result = []
20        
21        # Try every possible starting offset within a word length
22        for i in range(word_len):
23            left = i
24            right = i
25            current_count = {}
26            count = 0
27            
28            while right + word_len <= s_len:
29                word = s[right:right + word_len]
30                right += word_len
31                
32                if word in word_count:
33                    current_count[word] = current_count.get(word, 0) + 1
34                    count += 1
35                    
36                    # Shrink window from left if we have too many of this word
37                    while current_count[word] > word_count[word]:
38                        left_word = s[left:left + word_len]
39                        current_count[left_word] -= 1
40                        count -= 1
41                        left += word_len
42                    
43                    # Check if window contains exactly all words
44                    if count == num_words:
45                        result.append(left)
46                else:
47                    # Invalid word found, reset window
48                    current_count.clear()
49                    count = 0
50                    left = right
51        
52        return result
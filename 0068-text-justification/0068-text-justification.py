class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Determine how many words fit in this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # Words[i:j] go on this line
            num_words = j - i
            num_chars = sum(len(words[k]) for k in range(i, j))
            num_spaces = maxWidth - num_chars
            
            # Build the line
            if j == n or num_words == 1:
                # Last line or single word: left-justified
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # Middle line with multiple words: fully justified
                gaps = num_words - 1
                space_per_gap = num_spaces // gaps
                extra = num_spaces % gaps  # left slots get +1
                
                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    # Add spaces after this word
                    spaces_to_add = space_per_gap + (1 if k - i < extra else 0)
                    line += " " * spaces_to_add
                line += words[j - 1]  # last word has no trailing space
            
            res.append(line)
            i = j
        
        return res
class Solution(object):
    def maxNumOfSubstrings(self, s):
        first_occ = {}
        last_occ = {}
        for i, c in enumerate(s):
            if c not in first_occ:
                first_occ[c] = i
            last_occ[c] = i

        intervals = []
        for c, start in first_occ.items():
            end = last_occ[c]
            i = start
            valid = True
            while i <= end:
                ch = s[i]
                if first_occ[ch] < start:
                    valid = False
                    break
                end = max(end, last_occ[ch])
                i += 1
            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        return res
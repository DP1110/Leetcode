import bisect

class SummaryRanges(object):
    def __init__(self):
        self.starts = []  # sorted start values
        self.intervals = {}  # start -> end

    def addNum(self, value):
        starts = self.starts
        i = bisect.bisect_left(starts, value)

        if i < len(starts) and starts[i] == value:
            return
        if i > 0 and self.intervals[starts[i-1]] >= value - 1:
            left = i - 1
        elif i > 0 and self.intervals[starts[i-1]] == value - 1:
            left = i - 1
        else:
            left = None

        merge_left = i > 0 and self.intervals[starts[i-1]] >= value - 1
        merge_right = i < len(starts) and starts[i] == value + 1

        if merge_left and merge_right:
            ls = starts[i-1]
            rs = starts[i]
            self.intervals[ls] = self.intervals[rs]
            del self.intervals[rs]
            starts.pop(i)
        elif merge_left:
            ls = starts[i-1]
            self.intervals[ls] = max(self.intervals[ls], value)
        elif merge_right:
            rs = starts[i]
            self.intervals[value] = self.intervals[rs]
            del self.intervals[rs]
            starts[i] = value
        else:
            starts.insert(i, value)
            self.intervals[value] = value

    def getIntervals(self):
        return [[s, self.intervals[s]] for s in self.starts]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
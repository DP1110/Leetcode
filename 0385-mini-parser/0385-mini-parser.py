class Solution(object):
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        cur = None
        num_start = None

        for i, c in enumerate(s):
            if c == '[':
                if cur is not None:
                    stack.append(cur)
                cur = NestedInteger()
                num_start = None
            elif c == ']':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
                if stack:
                    parent = stack.pop()
                    parent.add(cur)
                    cur = parent
            elif c == ',':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
            else:  # digit or '-'
                if num_start is None:
                    num_start = i

        return cur
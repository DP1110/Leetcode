class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split("/")
        
        for part in parts:
            if part == "" or part == ".":
                # Skip empty strings (from consecutive slashes) and current dir
                continue
            elif part == "..":
                # Go up one directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory/file name (including "...")
                stack.append(part)
        
        # Join with single slashes and prepend leading slash
        return "/" + "/".join(stack)
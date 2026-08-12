1class Solution(object):
2    def levelOrder(self, root):
3        if not root:
4            return []
5        
6        result = []
7        queue = [root]
8        
9        while queue:
10            level_size = len(queue)
11            level = []
12            
13            for _ in range(level_size):
14                node = queue.pop(0)
15                level.append(node.val)
16                
17                if node.left:
18                    queue.append(node.left)
19                if node.right:
20                    queue.append(node.right)
21            
22            result.append(level)
23        
24        return result
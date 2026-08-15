1class Solution(object):
2    def cloneGraph(self, node):
3        if not node:
4            return None
5        
6        clones = {node: Node(node.val)}
7        queue = [node]
8        
9        while queue:
10            curr = queue.pop(0)
11            for neighbor in curr.neighbors:
12                if neighbor not in clones:
13                    clones[neighbor] = Node(neighbor.val)
14                    queue.append(neighbor)
15                clones[curr].neighbors.append(clones[neighbor])
16        
17        return clones[node]
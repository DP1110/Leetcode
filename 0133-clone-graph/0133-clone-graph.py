class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        clones = {node: Node(node.val)}
        queue = [node]
        
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])
        
        return clones[node]